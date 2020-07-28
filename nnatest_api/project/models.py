from django.db import models

from nnatest_api import settings


class Project(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="projects",
    )

    def __str__(self):
        return self.name
