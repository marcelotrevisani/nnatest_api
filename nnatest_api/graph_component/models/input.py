from django.db import models

from graph_component.models.node import Node


class Input(models.Model):
    node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name="inputs")
    name = models.CharField(max_length=150, null=True)
    arg_name = models.CharField(max_length=150)
    py_type = models.CharField(max_length=40, null=True)

    def __str__(self):
        return (
            f"{self.name if self.name else self.arg_name}"
            f" {self.py_type if self.py_type else 'Any'}"
        )
