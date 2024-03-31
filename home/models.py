from django.db import models

class UserProfile(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    major = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user_name
