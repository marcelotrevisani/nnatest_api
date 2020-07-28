from rest_framework import authentication, mixins, permissions, viewsets
from rest_framework.authentication import SessionAuthentication

from project.models import Project
from project.serializers import ProjectSerializers


class ProjectView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = ProjectSerializers
    authentication_classes = (authentication.TokenAuthentication, SessionAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Project.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by("name")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
