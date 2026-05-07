from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from unfold.admin import ModelAdmin

from apps.contact.models import ContactEnquiry
from apps.industries.models import Industry
from apps.services.models import Service

from .models import (
    AboutStripSettings,
    AddressSettings,
    CompanyIdentitySettings,
    HeroSectionSettings,
    SocialMediaSettings,
    StatsCountersSettings,
)


def dashboard_callback(request, context):
    context.update(
        {
            "services_total": Service.objects.filter(is_active=True).count(),
            "services_all": Service.objects.count(),
            "industries_total": Industry.objects.filter(is_active=True).count(),
            "industries_all": Industry.objects.count(),
            "enquiries_new": ContactEnquiry.objects.filter(
                status=ContactEnquiry.STATUS_NEW
            ).count(),
            "enquiries_read": ContactEnquiry.objects.filter(
                status=ContactEnquiry.STATUS_READ
            ).count(),
            "enquiries_replied": ContactEnquiry.objects.filter(
                status=ContactEnquiry.STATUS_REPLIED
            ).count(),
            "enquiries_total": ContactEnquiry.objects.count(),
            "recent_enquiries": ContactEnquiry.objects.select_related("service").order_by(
                "-created_at"
            )[:6],
        }
    )
    return context


def enquiry_badge(request):
    count = ContactEnquiry.objects.filter(status=ContactEnquiry.STATUS_NEW).count()
    return str(count) if count else None


class _SiteSettingsSectionAdmin(ModelAdmin):
    """Shared base for all SiteSettings proxy admins — singleton redirect + no add/delete."""

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        model_name = self.model._meta.model_name
        return HttpResponseRedirect(reverse(f"admin:core_{model_name}_change", args=[1]))


@admin.register(CompanyIdentitySettings)
class CompanyIdentitySettingsAdmin(_SiteSettingsSectionAdmin):
    fieldsets = (
        (
            "Company Identity",
            {
                "fields": (("name", "tagline"), ("email", "phone")),
            },
        ),
    )


@admin.register(AddressSettings)
class AddressSettingsAdmin(_SiteSettingsSectionAdmin):
    fieldsets = (
        (
            "Address",
            {
                "fields": (("address", "postal"), "domain"),
            },
        ),
    )


@admin.register(SocialMediaSettings)
class SocialMediaSettingsAdmin(_SiteSettingsSectionAdmin):
    fieldsets = (
        (
            "Social Media Links",
            {
                "fields": (("facebook_url", "twitter_url"), ("linkedin_url", "youtube_url")),
                "description": "Leave blank if not applicable. Icons only appear in the footer when a URL is set.",
            },
        ),
    )


@admin.register(HeroSectionSettings)
class HeroSectionSettingsAdmin(_SiteSettingsSectionAdmin):
    fieldsets = (
        (
            "Home Page — Hero Section",
            {
                "fields": (
                    "hero_headline",
                    "hero_subtext",
                    ("hero_cta_primary", "hero_cta_secondary"),
                ),
                "description": "The main banner text and call-to-action buttons on the home page.",
            },
        ),
    )


@admin.register(StatsCountersSettings)
class StatsCountersSettingsAdmin(_SiteSettingsSectionAdmin):
    fieldsets = (
        (
            "Home Page — Stats Counters",
            {
                "fields": (
                    ("stat_1_value", "stat_1_label"),
                    ("stat_2_value", "stat_2_label"),
                    ("stat_3_value", "stat_3_label"),
                    ("stat_4_value", "stat_4_label"),
                ),
                "description": "The four animated counters shown on the home page. Value can include symbols e.g. 50+, 24/7, 100%.",
            },
        ),
    )


@admin.register(AboutStripSettings)
class AboutStripSettingsAdmin(_SiteSettingsSectionAdmin):
    fieldsets = (
        (
            "Home Page — About Strip",
            {
                "fields": ("about_headline", "about_body"),
                "description": "The 'Who We Are' section on the home page.",
            },
        ),
    )
