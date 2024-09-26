from django.db import models # type: ignore
from django.conf import settings # type: ignore
from django.contrib.auth.models import AbstractUser # type: ignore

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.username
    

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    due_date = models.DateField( auto_now=False, auto_now_add=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    def __str__(self):
        return self.title


