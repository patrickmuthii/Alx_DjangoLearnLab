from django.db import models 
from django.conf import settings
from django.contrib.auth.models import AbstractUser 

# A custom user model with email as unique identifier
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.username
    
# A model for storing tasks
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
    
    RECURRING_CHOICES = [
        ('None', 'None'),
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
    ]

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    due_date = models.DateField( auto_now=False, auto_now_add=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    recurrence = models.CharField(max_length=20, choices=RECURRING_CHOICES, default='None')
    is_completed = models.BooleanField(default=False)
    def __str__(self):
        return self.title


