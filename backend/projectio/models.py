from django.db import models

from common.models import BaseModelWithUID

from .choices import StatusChoices


# Create your models here.
class Project(BaseModelWithUID):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=20, choices=StatusChoices.choices, default=StatusChoices.PENDING
    )

    def __str__(self):
        return self.name
