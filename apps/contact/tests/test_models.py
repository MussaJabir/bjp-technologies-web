import pytest

from apps.contact.models import ContactEnquiry
from apps.services.models import Service


@pytest.fixture
def service(db):
    return Service.objects.create(name="Cloud Infrastructure", order=1)


@pytest.fixture
def enquiry(db, service):
    return ContactEnquiry.objects.create(
        first_name="Amina",
        last_name="Hassan",
        email="amina@example.com",
        phone="+255700000001",
        company="TechCo",
        service=service,
        message="I'd like to discuss cloud migration.",
        ip_address="192.168.1.1",
        status=ContactEnquiry.STATUS_NEW,
    )


@pytest.mark.django_db
def test_str(enquiry):
    assert str(enquiry) == "Amina Hassan — amina@example.com"


@pytest.mark.django_db
def test_full_name(enquiry):
    assert enquiry.full_name == "Amina Hassan"


@pytest.mark.django_db
def test_status_defaults_to_new(db):
    e = ContactEnquiry.objects.create(
        first_name="Ali",
        last_name="Mwangi",
        email="ali@example.com",
        message="Hello there.",
    )
    assert e.status == ContactEnquiry.STATUS_NEW


@pytest.mark.django_db
def test_phone_and_company_optional(db):
    e = ContactEnquiry.objects.create(
        first_name="Juma",
        last_name="Said",
        email="juma@example.com",
        message="Just a quick question.",
    )
    assert e.phone == ""
    assert e.company == ""


@pytest.mark.django_db
def test_service_nullable(db):
    e = ContactEnquiry.objects.create(
        first_name="Test",
        last_name="User",
        email="test@example.com",
        message="No service selected.",
    )
    assert e.service is None


@pytest.mark.django_db
def test_timestamps_set(enquiry):
    assert enquiry.created_at is not None
    assert enquiry.updated_at is not None


@pytest.mark.django_db
def test_ip_address_stored(enquiry):
    assert enquiry.ip_address == "192.168.1.1"


@pytest.mark.django_db
def test_ordering_newest_first(db):
    e1 = ContactEnquiry.objects.create(
        first_name="A", last_name="A", email="a@a.com", message="First message."
    )
    e2 = ContactEnquiry.objects.create(
        first_name="B", last_name="B", email="b@b.com", message="Second message."
    )
    qs = list(ContactEnquiry.objects.all())
    assert qs[0] == e2
    assert qs[1] == e1
