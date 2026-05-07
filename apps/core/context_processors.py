from apps.industries.models import Industry
from apps.services.models import Service

from .models import SiteSettings


def company_info(request):
    settings = SiteSettings.get()
    return {
        "company": {
            "name": settings.name,
            "tagline": settings.tagline,
            "email": settings.email,
            "phone": settings.phone,
            "address": settings.address,
            "postal": settings.postal,
            "domain": settings.domain,
            "facebook_url": settings.facebook_url,
            "twitter_url": settings.twitter_url,
            "linkedin_url": settings.linkedin_url,
            "youtube_url": settings.youtube_url,
        },
        "footer_services": Service.objects.filter(is_active=True).order_by("order"),
        "footer_industries": Industry.objects.filter(is_active=True).order_by("order"),
    }
