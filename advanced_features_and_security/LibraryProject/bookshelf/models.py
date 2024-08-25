
# Create your models here.
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from .models import author

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['date_of_birth']

    objects = CustomUserManager()  

    def __str__(self):
        return self.username
    
#define custom permissions in models
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(author, on_delete=models.CASCADE, related_name = 'author')
    class meta:
        permissions = [
        ('can_create_book', 'can_create_book'),
        ('can_edit_book', 'can_edit_book'),
        ('can_delete_book', 'can_delete_book'),
        ('can_view_book', 'can_view_book'),
    ]

    def __str__(self):
        return self.title
      #create and configure groups
    