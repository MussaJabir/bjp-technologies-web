from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Service


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = ["name", "slug", "order", "is_active", "created_at"]
    list_filter = ["is_active"]
    search_fields = ["name", "tagline"]
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ["order", "is_active"]
    fieldsets = (
        ("Identity", {"fields": ("name", "slug", "tagline", "icon_svg", "order", "is_active")}),
        ("Content", {"fields": ("description", "bullet_points")}),
        ("Timestamps", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )
    readonly_fields = ["created_at", "updated_at"]
