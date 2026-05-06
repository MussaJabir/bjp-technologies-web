from wagtail.admin.panels import FieldPanel, FieldRowPanel, MultiFieldPanel
from wagtail.snippets.views.snippets import SnippetViewSet

from .models import Service


class ServiceSnippetViewSet(SnippetViewSet):
    model = Service
    menu_label = "Services"
    menu_icon = "list-ul"
    menu_order = 200
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
                FieldPanel("icon_svg"),
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
        FieldPanel("bullet_points"),
    ]


# Registered via WebsiteContentGroup in apps/core/wagtail_hooks.py
