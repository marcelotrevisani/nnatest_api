from rest_framework import authentication, mixins, permissions, viewsets
from rest_framework.authentication import SessionAuthentication

from runner.models.machine import Machine
from runner.serializers.machine_serializer import MachineSerializer


class MachineView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = MachineSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Machine.objects.all()

