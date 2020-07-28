from rest_framework import serializers

from runner.models.machine import Machine


class MachineSerializer(serializers.ModelSerializer):
    test_execution = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True, allow_empty=True
    )

    class Meta:
        model = Machine
        fields = (
            "id",
            "hostname",
            "release",
            "version",
            "machine",
            "manager",
            "test_execution",
        )
        read_only_fields = ("id", "test_execution")