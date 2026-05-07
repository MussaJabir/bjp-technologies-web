from apps.industries.models import Industry
from apps.services.models import Service

from .models import SiteSettings


def company_info(request):
    site = SiteSettings.get()
    return {
        "company": site,
        "footer_services": Service.objects.filter(is_active=True).order_by("order"),
        "footer_industries": Industry.objects.filter(is_active=True).order_by("order"),
    }
