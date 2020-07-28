from rest_framework import mixins, viewsets
from rest_framework.authentication import SessionAuthentication, \
    TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from graph_component.models.input import Input
from graph_component.serializers.input_serializer import InputSerializers


class InputView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Input.objects.all()
    serializer_class = InputSerializers

    # def get_queryset(self):
    #     return self.queryset.filter(project__user=self.request.user)
