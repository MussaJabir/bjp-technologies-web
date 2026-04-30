from django.contrib import admin

from .models import Industry


@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "order", "is_active", "created_at"]
    list_filter = ["is_active"]
    search_fields = ["name", "tagline"]
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ["order", "is_active"]
    fieldsets = (
        ("Identity", {"fields": ("name", "slug", "tagline", "image", "order", "is_active")}),
        ("Content", {"fields": ("description", "services_offered")}),
        ("Timestamps", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )
    readonly_fields = ["created_at", "updated_at"]
