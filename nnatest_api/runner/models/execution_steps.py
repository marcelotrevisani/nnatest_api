from django.db import models

from runner.models.execution import Execution


class ExecutionSteps(models.Model):
    step = models.CharField(max_length=20, choices=("collection", "setup", "call", "teardown"))
    result = models.CharField(max_length=20, choices=("pass", "fail", "skip"), null=True)
    duration = models.FloatField(null=True)
    error_msg = models.TextField(null=True)
    extra_info = models.TextField(null=True)
    execution = models.ForeignKey(
        Execution, on_delete=models.CASCADE, related_name="execution_steps"
    )

    def __str__(self):
        return self.step
