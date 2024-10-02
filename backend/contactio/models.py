from django.db import models

from common.models import BaseModelWithUID


# Create your models here.
class Contact(BaseModelWithUID):
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
