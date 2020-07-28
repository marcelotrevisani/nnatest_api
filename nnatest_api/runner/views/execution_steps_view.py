from rest_framework import authentication, mixins, permissions, viewsets

from runner.models.execution_steps import ExecutionSteps
from runner.serializers.execution_steps_serializer import ExecutionStepsSerializer


class ExecutionStepsView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = ExecutionStepsSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ExecutionSteps.objects.all()

