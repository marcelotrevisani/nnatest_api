import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from graph_component.models.edge import Edge
from graph_component.models.node import Node
from project.models import Project


CREATE_EDGE = reverse("graph_component:edge-list")


@pytest.mark.django_db
def test_create_edge():
    user = get_user_model().objects.create_user(
        email="user@test.com", password="pass123", name="User test"
    )
    APIClient().force_authenticate(user=user)
    project = Project.objects.create(name="Project 1", user=user)
    node1 = Node.objects.create(
        name="Node1",
        description="Node description",
        name_component_builtin="sum_num",
        project=project,
        x_position=1.1,
        y_position=2.2,
        height=3.3,
        width=4.4,
    )
    node2 = Node.objects.create(
        name="Node2",
        description="Node description",
        name_component_builtin="sum_num",
        project=project,
        x_position=1.1,
        y_position=2.2,
        height=3.3,
        width=4.4,
    )
    Edge.objects.create(node_parent=node1, node_child=node2)
    assert str(Edge.objects.all()[0]) == "Node1 -> Node2"
    assert Edge.objects.all()[0].node_parent == node1
    assert Edge.objects.all()[0].node_child == node2


@pytest.mark.django_db
def test_create_edge_view():
    user = get_user_model().objects.create_user(
        email="user@test.com", password="pass123", name="User test"
    )
    client_api = APIClient()
    client_api.force_authenticate(user=user)
    project = Project.objects.create(name="Project 1", user=user)
    node1 = Node.objects.create(
        name="Node1",
        description="Node description",
        name_component_builtin="sum_num",
        project=project,
        x_position=1.1,
        y_position=2.2,
        height=3.3,
        width=4.4,
    )
    node2 = Node.objects.create(
        name="Node2",
        description="Node description",
        name_component_builtin="sum_num",
        project=project,
        x_position=1.1,
        y_position=2.2,
        height=3.3,
        width=4.4,
    )
    res = client_api.post(CREATE_EDGE, {"parent": node1.id, "child": node2.id})
    assert res.status_code == status.HTTP_201_CREATED
