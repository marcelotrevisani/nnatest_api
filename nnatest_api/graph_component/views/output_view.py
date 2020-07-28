from rest_framework import mixins, viewsets
from rest_framework.authentication import SessionAuthentication, \
    TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from graph_component.models.output import Output
from graph_component.serializers.output_serializer import OutputSerializers


class OutputView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, )
    queryset = Output.objects.all()
    serializer_class = OutputSerializers

    # def get_queryset(self):
    #     return self.queryset.filter(project__user=self.request.user)
