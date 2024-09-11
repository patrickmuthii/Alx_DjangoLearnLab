from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank = True)
    image = models.URLField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank = True)
    image = models.URLField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'