from django.urls import path

from . import views

app_name = "industries"

urlpatterns = [
    path("", views.IndustriesListView.as_view(), name="list"),
    path("<slug:slug>/", views.IndustryDetailView.as_view(), name="detail"),
]
