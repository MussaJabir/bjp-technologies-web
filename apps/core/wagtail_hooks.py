from django.templatetags.static import static
from django.utils.html import format_html
from wagtail import hooks
from wagtail.admin.ui.components import Component


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
def add_enquiries_panel(request, panels):
    panels.append(EnquiriesDashboardPanel())


@hooks.register("insert_global_admin_css")
def global_admin_css():
    return format_html(
        '<link rel="stylesheet" href="{}">',
        static("css/wagtail_brand.css"),
    )
