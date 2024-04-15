from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pics = models.ImageField(upload_to='profile_pics/', default='default.jpg')

    def __str__(self):
        return self.user.username
