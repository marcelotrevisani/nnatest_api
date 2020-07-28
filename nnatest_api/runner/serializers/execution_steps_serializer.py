from rest_framework import serializers

from runner.models.execution_steps import ExecutionSteps


class ExecutionStepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecutionSteps
        fields = (
            "id",
            "step",
            "result",
            "duration",
            "error_msg",
            "extra_info",
            "execution",
        )
        read_only_fields = ("id",)