import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SiteSettings(models.Model):
    """Singleton — only one row ever exists. Edit via admin, never create a second."""

    name = models.CharField(max_length=120, default="BJP Technologies (T) Limited")
    tagline = models.CharField(max_length=200, default="Secure Technology. Scalable Growth.")
    email = models.EmailField(default="info@bjptechnologies.co.tz")
    phone = models.CharField(max_length=30, default="+255 678 290 994")
    address = models.CharField(max_length=200, default="Ubungo – Dar es Salaam, Tanzania")
    postal = models.CharField(max_length=100, default="P.O Box 7276, Msakuzi – Mbezi")
    domain = models.CharField(max_length=100, default="bjptechnologies.co.tz")

    facebook_url = models.URLField(blank=True, default="")
    twitter_url = models.URLField(blank=True, default="")
    linkedin_url = models.URLField(blank=True, default="")
    youtube_url = models.URLField(blank=True, default="")

    # Home page — Hero
    hero_headline = models.CharField(max_length=200, default="Secure Technology. Scalable Growth.")
    hero_subtext = models.TextField(
        default=(
            "Tanzania's trusted IT partner — delivering tailored software, cybersecurity, "
            "cloud, and payment integration solutions that drive real business growth."
        )
    )
    hero_cta_primary = models.CharField(max_length=60, default="Get Free Consultation")
    hero_cta_secondary = models.CharField(max_length=60, default="Our Services")

    # Home page — Stats counters
    stat_1_value = models.CharField(max_length=20, default="7")
    stat_1_label = models.CharField(max_length=60, default="IT Service Lines")
    stat_2_value = models.CharField(max_length=20, default="6")
    stat_2_label = models.CharField(max_length=60, default="Industries Served")
    stat_3_value = models.CharField(max_length=20, default="24/7")
    stat_3_label = models.CharField(max_length=60, default="Monitoring & Support")
    stat_4_value = models.CharField(max_length=20, default="100%")
    stat_4_label = models.CharField(max_length=60, default="Dedicated to Your Success")

    # Home page — About strip
    about_headline = models.CharField(
        max_length=200, default="Tanzania's IT Partner Built for East Africa"
    )
    about_body = models.TextField(
        default=(
            "BJP Technologies (T) Limited is a full-service IT company headquartered in "
            "Ubungo, Dar es Salaam. We build and maintain the software, infrastructure, "
            "and security systems that keep growing businesses running — from Tanzanian "
            "startups to regional enterprises."
        )
    )

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self) -> str:
        return "Site Settings"

    def save(self, *args, **kwargs) -> None:
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get(cls) -> "SiteSettings":
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj
