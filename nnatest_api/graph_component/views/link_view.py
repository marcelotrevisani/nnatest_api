from rest_framework import mixins, viewsets
from rest_framework.authentication import SessionAuthentication, \
    TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from graph_component.models.link import Link
from graph_component.serializers.link_serializer import LinkSerializers


class LinkView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Link.objects.all()
    serializer_class = LinkSerializers

    # def get_queryset(self):
    #     return self.queryset.filter(project__user=self.request.user)
