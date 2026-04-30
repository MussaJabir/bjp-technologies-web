import pytest


@pytest.mark.django_db
def test_home_page_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_about_page_returns_200(client):
    response = client.get("/about/")
    assert response.status_code == 200
