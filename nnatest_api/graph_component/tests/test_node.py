import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from graph_component.models.node import Node
from project.models import Project


@pytest.mark.django_db
def test_create_node():
    user = get_user_model().objects.create_user(
        email="user@test.com", password="pass123", name="User test"
    )
    APIClient().force_authenticate(user=user)
    project = Project.objects.create(name="Project 1", user=user)

    node = Node.objects.create(
        name="Node1",
        description="Node description",
        name_component_builtin="sum_num",
        project=project,
        x_position=1.1,
        y_position=2.2,
        height=3.3,
        width=4.4,
    )
    assert str(node) == "Node1"
    assert Node.objects.filter(project=project).values()[0]["name"] == "Node1"
    assert Node.objects.filter(project=project).values()[0]["id"] == node.id
