import pytest

from apps.industries.models import Industry


@pytest.mark.django_db
class TestIndustryModel:
    def test_str(self):
        ind = Industry.objects.create(name="Healthcare")
        assert str(ind) == "Healthcare"

    def test_slug_auto_generated(self):
        ind = Industry.objects.create(name="Financial Institutions")
        assert ind.slug == "financial-institutions"

    def test_slug_not_overwritten_on_save(self):
        ind = Industry.objects.create(name="Healthcare", slug="custom-slug")
        ind.save()
        assert ind.slug == "custom-slug"

    def test_get_services_list_empty(self):
        ind = Industry.objects.create(name="Empty", services_offered="")
        assert ind.get_services_list() == []

    def test_get_services_list_parsed(self):
        ind = Industry.objects.create(
            name="Fintech",
            services_offered="SACCOS software\nMobile banking\nPayment gateway",
        )
        assert ind.get_services_list() == ["SACCOS software", "Mobile banking", "Payment gateway"]

    def test_get_services_list_strips_blank_lines(self):
        ind = Industry.objects.create(
            name="NGO",
            services_offered="Grant tracking\n\nReport generation\n",
        )
        assert ind.get_services_list() == ["Grant tracking", "Report generation"]

    def test_default_is_active_true(self):
        ind = Industry.objects.create(name="Active")
        assert ind.is_active is True

    def test_has_timestamps(self):
        ind = Industry.objects.create(name="Timestamped")
        assert ind.created_at is not None
        assert ind.updated_at is not None
