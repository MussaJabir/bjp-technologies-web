from django.urls import path
from django.views.generic import TemplateView

app_name = "industries"

urlpatterns = [
    path("", TemplateView.as_view(template_name="industries/list.html"), name="list"),
    path(
        "<slug:slug>/", TemplateView.as_view(template_name="industries/detail.html"), name="detail"
    ),
]
