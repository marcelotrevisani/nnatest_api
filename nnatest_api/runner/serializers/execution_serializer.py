from rest_framework import serializers

from runner.models.execution import Execution


class ExecutionSerializer(serializers.ModelSerializer):
    execution_steps = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True, allow_empty=True
    )
    class Meta:
        model = Execution
        fields = (
            "id",
            "pytest_id",
            "pytest_node",
            "machine",
            "execution_steps",
        )
        read_only_fields = ("id", "execution_steps")