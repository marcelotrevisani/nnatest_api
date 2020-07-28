from rest_framework import mixins, viewsets
from rest_framework.authentication import SessionAuthentication, \
    TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from graph_component.models.node import Node
from graph_component.serializers.node_serializer import NodeSerializers


class NodeView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Node.objects.all()
    serializer_class = NodeSerializers

    def get_queryset(self):
        # projects = Project.objects.filter(user=self.request.user)
        return self.queryset.filter(project__user=self.request.user)

    # def perform_create(self, serializer):
    #     serializer.save(project=self.request)



