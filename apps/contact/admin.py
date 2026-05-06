from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import ContactEnquiry


@admin.register(ContactEnquiry)
class ContactEnquiryAdmin(ModelAdmin):
    list_display = [
        "full_name",
        "email",
        "phone",
        "company",
        "service",
        "status",
        "created_at",
    ]
    list_filter = ["status", "service", "created_at"]
    search_fields = ["first_name", "last_name", "email", "company", "message"]
    readonly_fields = ["id", "ip_address", "created_at", "updated_at"]
    list_editable = ["status"]
    ordering = ["-created_at"]
    fieldsets = [
        (
            "Contact Details",
            {
                "fields": [
                    "first_name",
                    "last_name",
                    "email",
                    "phone",
                    "company",
                    "service",
                ]
            },
        ),
        (
            "Enquiry",
            {"fields": ["message", "status"]},
        ),
        (
            "Meta",
            {
                "fields": ["id", "ip_address", "created_at", "updated_at"],
                "classes": ["collapse"],
            },
        ),
    ]
