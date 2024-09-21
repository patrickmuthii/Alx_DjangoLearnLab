from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#custm user model

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(blank=True, null=True)
    followers = models.ManyToManyField("self", blank=True, symmetrical=False, related_name="following")
    foollowing = models.ManyToManyField("self", blank=True, symmetrical=False, related_name="followers")
    def __str__(self):
        return self.username

