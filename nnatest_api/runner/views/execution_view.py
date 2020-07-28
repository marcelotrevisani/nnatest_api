from rest_framework import authentication, mixins, permissions, viewsets

from runner.models.execution import Execution
from runner.serializers.execution_serializer import ExecutionSerializer


class ExecutionView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = ExecutionSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Execution.objects.all()

