from rest_framework import mixins, viewsets
from rest_framework.authentication import SessionAuthentication, \
    TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from graph_component.models.edge import Edge
from graph_component.models.node import Node
from graph_component.serializers.edge_serializer import EdgeSerializers
from project.models import Project


class EdgeView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Edge.objects.all()
    serializer_class = EdgeSerializers

    def get_queryset(self):
        projects = Project.objects.filter(user=self.request.user)
        nodes = Node.objects.filter(project__in=projects)
        node_parents = self.queryset.filter(parent__in=nodes)
        node_children = self.queryset.filter(child__in=nodes)
        return node_parents.union(node_children)
