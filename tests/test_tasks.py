import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from users.models import User
from projects.models import Project
from tasks.models import Task

@pytest.mark.django_db
def test_create_task():
    user = User.objects.create_user(username="taskuser", password="pass1234")
    project = Project.objects.create(owner=user, name="Demo", description="Desc")
    client = APIClient()

    token_resp = client.post(reverse('token_obtain_pair'), {"username": "taskuser", "password": "pass1234"})
    token = token_resp.data["access"]
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    data = {
        "project": project.id,
        "title": "New Task",
        "description": "Task description",
        "status": "pending"
    }
    response = client.post("/api/tasks/", data, format='json')
    assert response.status_code == 201
    assert response.data["title"] == "New Task"


@pytest.mark.django_db
def test_get_tasks_list():
    user = User.objects.create_user(username="tasklist", password="pass1234")
    project = Project.objects.create(owner=user, name="Demo", description="Desc")
    Task.objects.create(
        project=project,
        title="Existing Task",
        description="Already there"
    )

    client = APIClient()
    token_resp = client.post(
        reverse('token_obtain_pair'),
        {"username": "tasklist", "password": "pass1234"}
    )
    token = token_resp.data["access"]
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    response = client.get("/api/tasks/")
    assert response.status_code == 200
    assert any(task["title"] == "Existing Task" for task in response.data)
