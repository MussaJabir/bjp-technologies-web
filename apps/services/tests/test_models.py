import pytest

from apps.services.models import Service


@pytest.mark.django_db
class TestServiceModel:
    def test_str(self):
        svc = Service.objects.create(name="Test Service")
        assert str(svc) == "Test Service"

    def test_slug_auto_generated(self):
        svc = Service.objects.create(name="Cloud Migration")
        assert svc.slug == "cloud-migration"

    def test_slug_not_overwritten_on_save(self):
        svc = Service.objects.create(name="Cloud Migration", slug="custom-slug")
        svc.save()
        assert svc.slug == "custom-slug"

    def test_get_bullet_list_empty(self):
        svc = Service.objects.create(name="No Bullets", bullet_points="")
        assert svc.get_bullet_list() == []

    def test_get_bullet_list_parsed(self):
        svc = Service.objects.create(
            name="With Bullets", bullet_points="Item one\nItem two\nItem three"
        )
        assert svc.get_bullet_list() == ["Item one", "Item two", "Item three"]

    def test_get_bullet_list_strips_blank_lines(self):
        svc = Service.objects.create(name="Blanks", bullet_points="Item one\n\nItem two\n")
        assert svc.get_bullet_list() == ["Item one", "Item two"]

    def test_default_is_active_true(self):
        svc = Service.objects.create(name="Active")
        assert svc.is_active is True

    def test_has_created_at_and_updated_at(self):
        svc = Service.objects.create(name="Timestamped")
        assert svc.created_at is not None
        assert svc.updated_at is not None
