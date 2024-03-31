from django.db import models
from django.contrib.auth.models import AbstractUser

class User(models.Model):
    username = models.CharField(max_length = 15, unique=True)
    password = models.CharField(max_length = 15)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.username = self.id
        super().save(*args, **kwargs)
