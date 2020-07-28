from django.db import models

from runner.models.machine import Machine


class Execution(models.Model):
    pytest_id = models.CharField(max_length=255)
    pytest_node = models.CharField(max_length=255)
    machine = models.ForeignKey(
        Machine, on_delete=models.CASCADE, related_name="test_execution"
    )

    def __str__(self):
        return self.pytest_id
