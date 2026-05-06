from wagtail.admin.panels import FieldPanel, FieldRowPanel, MultiFieldPanel
from wagtail.snippets.views.snippets import SnippetViewSet

from .models import Industry


class IndustrySnippetViewSet(SnippetViewSet):
    model = Industry
    menu_label = "Industries"
    menu_icon = "tag"
    menu_order = 210
    list_display = ["name", "tagline", "order", "is_active"]
    list_filter = ["is_active"]
    search_fields = ["name", "tagline", "description"]
    ordering = ["order", "name"]

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("name"),
                FieldPanel("slug"),
                FieldPanel("tagline"),
                FieldPanel("image"),
                FieldRowPanel(
                    [
                        FieldPanel("order"),
                        FieldPanel("is_active"),
                    ]
                ),
            ],
            heading="Identity",
        ),
        FieldPanel("description"),
        FieldPanel("services_offered"),
    ]


# Registered via WebsiteContentGroup in apps/core/wagtail_hooks.py
