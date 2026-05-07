from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from unfold.admin import ModelAdmin

from apps.contact.models import ContactEnquiry
from apps.industries.models import Industry
from apps.services.models import Service

from .models import SiteSettings


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


@admin.register(SiteSettings)
class SiteSettingsAdmin(ModelAdmin):
    fieldsets = (
        (
            "Company Identity",
            {
                "fields": (("name", "tagline"), ("email", "phone")),
            },
        ),
        (
            "Address",
            {
                "fields": (("address", "postal"), "domain"),
            },
        ),
        (
            "Social Media Links",
            {
                "fields": (("facebook_url", "twitter_url"), ("linkedin_url", "youtube_url")),
                "classes": ("collapse",),
                "description": "Leave blank if not applicable.",
            },
        ),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        """Redirect the list view straight to the edit form."""
        return HttpResponseRedirect(reverse("admin:core_sitesettings_change", args=[1]))
