from django.templatetags.static import static
from django.utils.html import format_html
from wagtail import hooks
from wagtail.admin.ui.components import Component
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSetGroup

from apps.industries.wagtail_hooks import IndustrySnippetViewSet
from apps.services.wagtail_hooks import ServiceSnippetViewSet

# ── Content group: Services + Industries under one sidebar item ──────────────


class WebsiteContentGroup(SnippetViewSetGroup):
    menu_label = "Website Content"
    menu_icon = "folder-open-inverse"
    menu_order = 200
    items = (ServiceSnippetViewSet, IndustrySnippetViewSet)


register_snippet(WebsiteContentGroup)


# ── Dashboard panel: site-wide stats (services, industries, enquiries) ────────


class SiteStatsDashboardPanel(Component):
    name = "bjp_site_stats"
    template_name = "core/wagtail/dashboard_stats.html"
    order = 30

    def get_context_data(self, parent_context):
        from apps.contact.models import ContactEnquiry
        from apps.industries.models import Industry
        from apps.services.models import Service

        return {
            "services_total": Service.objects.filter(is_active=True).count(),
            "services_all": Service.objects.count(),
            "industries_total": Industry.objects.filter(is_active=True).count(),
            "industries_all": Industry.objects.count(),
            "enquiries_new": ContactEnquiry.objects.filter(
                status=ContactEnquiry.STATUS_NEW
            ).count(),
            "enquiries_total": ContactEnquiry.objects.count(),
        }


# ── Dashboard panel: recent enquiries ────────────────────────────────────────


class EnquiriesDashboardPanel(Component):
    name = "bjp_enquiries"
    template_name = "core/wagtail/dashboard_enquiries.html"
    order = 50

    def get_context_data(self, parent_context):
        from apps.contact.models import ContactEnquiry

        return {
            "new_count": ContactEnquiry.objects.filter(status=ContactEnquiry.STATUS_NEW).count(),
            "read_count": ContactEnquiry.objects.filter(status=ContactEnquiry.STATUS_READ).count(),
            "replied_count": ContactEnquiry.objects.filter(
                status=ContactEnquiry.STATUS_REPLIED
            ).count(),
            "recent": ContactEnquiry.objects.select_related("service").all()[:5],
        }


@hooks.register("construct_homepage_panels")
def customize_dashboard(request, panels):
    # Remove the default "What's new in Wagtail" panel — not relevant here
    panels[:] = [p for p in panels if getattr(p, "name", "") != "whats_new_in_wagtail_version"]
    panels.append(SiteStatsDashboardPanel())
    panels.append(EnquiriesDashboardPanel())


# ── Strip out Wagtail-default menu items not needed for BJP admin ─────────────


@hooks.register("construct_main_menu")
def clean_main_menu(request, menu_items):
    # Remove: Pages tree, Images library, Documents, Reports — none of these are used
    hidden = {"explorer", "images", "documents", "reports"}
    menu_items[:] = [item for item in menu_items if item.name not in hidden]


@hooks.register("construct_settings_menu")
def clean_settings_menu(request, menu_items):
    # Keep only: Sites configuration and URL Redirects
    keep = {"sites", "redirects"}
    menu_items[:] = [item for item in menu_items if item.name in keep]


# ── BJP brand CSS injected into every admin page ─────────────────────────────


@hooks.register("insert_global_admin_css")
def global_admin_css():
    return format_html(
        '<link rel="stylesheet" href="{}">',
        static("css/wagtail_brand.css"),
    )
