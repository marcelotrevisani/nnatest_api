from django.db import models

from runner.models.manager import Manager


class Machine(models.Model):
    hostname = models.CharField(max_length=100)
    release = models.CharField(max_length=150)
    version = models.CharField(max_length=200)
    machine = models.CharField(max_length=100)
    manager = models.ForeignKey(
        Manager, on_delete=models.CASCADE, related_name="machines"
    )

    def __str__(self):
        return self.hostname