from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from apps.industries.models import Industry
from apps.services.models import Service


class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return ["main:home", "main:about", "services:list", "industries:list", "contact:contact"]

    def location(self, item):
        return reverse(item)


class ServiceSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return Service.objects.filter(is_active=True)

    def location(self, obj):
        return reverse("services:detail", kwargs={"slug": obj.slug})


class IndustrySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return Industry.objects.filter(is_active=True)

    def location(self, obj):
        return reverse("industries:detail", kwargs={"slug": obj.slug})
