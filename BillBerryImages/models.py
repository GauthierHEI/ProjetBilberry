from django.db import models

# Create your models here.

import datetime
from django.utils import timezone


class Image(models.Model):
    verified = models.BooleanField(default=False)
    rejected = models.NullBooleanField(default=None)
    name = models.CharField(max_length=200)
    upload_time = models.DateTimeField("date uploaded", default=timezone.now)
    image = models.ImageField(upload_to="documents/")
    # This model will be used to stock everything we need in the database

    def __str__(self):
        return self.name
