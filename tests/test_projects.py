import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from users.models import User

@pytest.mark.django_db
def test_create_project():
    user = User.objects.create_user(username="projuser", password="pass1234")
    client = APIClient()

    # login & token al
    token_resp = client.post(reverse('token_obtain_pair'), {"username": "projuser", "password": "pass1234"})
    token = token_resp.data["access"]

    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    data = {"name": "My Project", "description": "Test project"}
    response = client.post("/api/projects/", data, format='json')
    assert response.status_code == 201
    assert response.data["name"] == "My Project"


@pytest.mark.django_db
def test_get_projects_list():
    client = APIClient()
    response = client.get("/api/projects/")
    assert response.status_code == 200
