from rest_framework import serializers

from project.models import Project


class ProjectSerializers(serializers.ModelSerializer):
    nodes = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True, allow_empty=True
    )

    class Meta:
        model = Project
        fields = ("id", "name", "user", "nodes")
        read_only_fields = ("id", "user", "nodes")


class ProjectPKField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return Project.objects.filter(user=self.context["request"].user)
