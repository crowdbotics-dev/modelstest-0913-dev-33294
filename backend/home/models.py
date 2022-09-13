from django.conf import settings
from django.db import models


class Pet(models.Model):
    "Generated Model"
    nickname = models.CharField(
        max_length=100,
    )
    age = models.IntegerField()
    breed = models.CharField(
        max_length=100,
    )
    gender = models.CharField(
        max_length=100,
    )
    description = models.TextField()
