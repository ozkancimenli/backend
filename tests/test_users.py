import pytest
from rest_framework.test import APIClient
from django.urls import reverse

@pytest.mark.django_db
def test_user_registration():
    client = APIClient()
    url = reverse('user-register')
    data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "Testpass123!",
        "password2": "Testpass123!"
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 201
    assert "username" in response.data


@pytest.mark.django_db
def test_user_login():
    client = APIClient()
    # önce kullanıcı oluştur
    client.post(reverse('user-register'), {
        "username": "loginuser",
        "email": "login@example.com",
        "password": "Testpass123!",
        "password2": "Testpass123!"
    }, format='json')

    # token al
    url = reverse('token_obtain_pair')
    data = {"username": "loginuser", "password": "Testpass123!"}
    response = client.post(url, data, format='json')
    assert response.status_code == 200
    assert "access" in response.data
