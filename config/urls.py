from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.main.urls", namespace="main")),
    path("services/", include("apps.services.urls", namespace="services")),
    path("industries/", include("apps.industries.urls", namespace="industries")),
    path("contact/", include("apps.contact.urls", namespace="contact")),
]
