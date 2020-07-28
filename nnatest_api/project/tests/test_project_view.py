import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


CREATE_PROJECT = reverse("project:project-list")


@pytest.fixture
def user_authenticated(client_api):
    user = get_user_model().objects.create_user(
        email="user@test.com", password="pass123", name="User test"
    )
    client_api.force_authenticate(user=user)
    return user


@pytest.fixture
def client_api():
    return APIClient()


@pytest.mark.django_db
def test_project_api(user_authenticated, client_api):
    payload = {"name": "project_api"}
    project = client_api.post(CREATE_PROJECT, payload)
    assert project.status_code == status.HTTP_201_CREATED
    assert project.data["name"] == "project_api"
    assert project.data["user"] == user_authenticated.id


@pytest.mark.django_db
def test_list_project(user_authenticated, client_api):
    project1 = client_api.post(CREATE_PROJECT, {"name": "project1"})
    assert project1.status_code == status.HTTP_201_CREATED
    project2 = client_api.post(CREATE_PROJECT, {"name": "project2"})
    assert project2.status_code == status.HTTP_201_CREATED

    res = client_api.get(CREATE_PROJECT)
    assert res.status_code == status.HTTP_200_OK
    assert len(res.data) == 2
    res_data = sorted(res.data, key=lambda x: x["name"])
    assert res_data[0]["name"] == "project1"
    assert res_data[0]["user"] == user_authenticated.id
    assert res_data[1]["name"] == "project2"
    assert res_data[1]["user"] == user_authenticated.id