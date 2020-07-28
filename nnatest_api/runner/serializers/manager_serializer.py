from rest_framework import serializers

from runner.models.manager import Manager


class ManagerSerializer(serializers.ModelSerializer):
    machines = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True, allow_empty=True
    )

    class Meta:
        model = Manager
        fields = ("id", "project", "machines", "name")
        read_only_fields = ("id", "machines")
