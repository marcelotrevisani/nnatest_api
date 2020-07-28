from django.db import models

from project.models import Project


class Node(models.Model):
    name = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True)
    name_component_builtin = models.CharField(max_length=150, null=False)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="nodes"
    )
    x_position = models.FloatField(null=True)
    y_position = models.FloatField(null=True)
    height = models.FloatField(null=True)
    width = models.FloatField(null=True)

    def __str__(self):
        return self.name if self.name else self.name_component_builtin
