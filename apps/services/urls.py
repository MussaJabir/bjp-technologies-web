from django.urls import path
from django.views.generic import TemplateView

app_name = "services"

urlpatterns = [
    path("", TemplateView.as_view(template_name="services/list.html"), name="list"),
    path("<slug:slug>/", TemplateView.as_view(template_name="services/detail.html"), name="detail"),
]
