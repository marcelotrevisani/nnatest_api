import pytest
from django.contrib.auth import get_user_model

from project import models
from user import models as user_models


@pytest.mark.django_db
def test_create_project():
    assert models.Project.objects.count() == 0
    assert user_models.User.objects.count() == 0
    user = get_user_model().objects.create_user("test@servidor.com", "pass123")
    new_project = models.Project.objects.create(user=user, name="project1")

    assert models.Project.objects.count() == 1
    assert user_models.User.objects.count() == 1
    assert new_project.name == "project1"
    assert new_project.user == user


@pytest.mark.django_db
def test_projects_in_users():
    user1 = get_user_model().objects.create_user("user1@imgtec.com", "pass123")
    user2 = get_user_model().objects.create_user("user2@imgtec.com", "pass123")
    get_user_model().objects.create_user("user3@imgtec.com", "pass123")
    project1 = models.Project.objects.create(user=user1, name="project1")
    project2 = models.Project.objects.create(user=user1, name="project2")
    project3 = models.Project.objects.create(user=user2, name="project3")

    assert models.Project.objects.filter(user=user2).values()[0]["id"] == project3.id
    assert len(models.Project.objects.filter(user=user2).values()) == 1
    all_projects_user1 = models.Project.objects.filter(user=user1).order_by("id").values()
    assert len(all_projects_user1) == 2
    assert all_projects_user1[0]["id"] == project1.id
    assert all_projects_user1[1]["id"] == project2.id

