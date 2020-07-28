from django.db import models

from project.models import Project


class Manager(models.Model):
    name = models.CharField(max_length=255, null=True)
    # start_time = models.DateTimeField()
    # end_time = models.DateTimeField()
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="test_managers", null=True
    )

    def __str__(self):
        return self.name if self.name else self.id
