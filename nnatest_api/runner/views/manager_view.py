from rest_framework import authentication, mixins, permissions, viewsets

from runner.models.manager import Manager
from runner.serializers.manager_serializer import ManagerSerializer


class ManagerView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = ManagerSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Manager.objects.all()

