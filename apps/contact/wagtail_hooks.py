from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from .models import ContactEnquiry


class ContactEnquirySnippetViewSet(SnippetViewSet):
    model = ContactEnquiry
    menu_label = "Enquiries"
    menu_icon = "mail"
    menu_order = 300
    list_display = ["full_name", "email", "service", "status", "created_at"]
    list_filter = ["status", "service"]
    search_fields = ["first_name", "last_name", "email", "company", "message"]
    ordering = ["-created_at"]
    inspect_view_enabled = True
    inspect_view_fields = [
        "first_name",
        "last_name",
        "email",
        "phone",
        "company",
        "service",
        "message",
        "ip_address",
        "status",
        "created_at",
    ]

    # Edit view only exposes the status field — all other data is read via inspect view
    panels = [
        MultiFieldPanel(
            [
                FieldPanel("first_name", read_only=True),
                FieldPanel("last_name", read_only=True),
                FieldPanel("email", read_only=True),
                FieldPanel("phone", read_only=True),
                FieldPanel("company", read_only=True),
                FieldPanel("service", read_only=True),
            ],
            heading="Contact Details",
        ),
        FieldPanel("message", read_only=True),
        MultiFieldPanel(
            [
                FieldPanel("status"),
                FieldPanel("ip_address", read_only=True),
            ],
            heading="Status & Meta",
        ),
    ]


register_snippet(ContactEnquirySnippetViewSet)
