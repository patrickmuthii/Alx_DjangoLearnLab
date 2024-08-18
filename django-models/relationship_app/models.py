# from django.db import models
# django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# # Create your models here.

# class Author(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name
    

# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.title

# class Library(models.Model):
#         name = models.CharField(max_length=100)
#         books = models.ManyToManyField(Book)

#         def __str__(self):
#             return self.name
        
# class Librarian(models.Model):
#     name = models.CharField(max_length=100)
#     library = models.OneToOneField(Library, on_delete=models.CASCADE)  

#     def __str__(self):
#         return self.name
    
# class UserProfile(models.Model):
#      user = models.OneToOneField(User, on_delete=models.CASCADE)



#      Role_Choices =(
#         ('Admin','Admin'),
#         ('Librarian', 'Librarian'),
#         ('Member', 'Member'),
    
#     )
    
# role = models.CharField(max_length=50,  choices='Role_Choices')
# userprofile = models.TextField()

# def __str__(self):
#     return f'{self.user.username} - {self.role}'

# #Signal to automatically create a UserProfile when a new User is created
# from django.db.models.signals import post_save
# from django.dispatch import receiver


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.userprofile.save()    

from django.urls import path
from .views import list_books, LibraryDetailView, index
from django.contrib.auth.views import LoginView, LogoutView
from . import views
urlpatterns = [
    path("list_books/", list_books, name="list_books"),
    path("library_detail/", LibraryDetailView.as_view(), name="library_detail"),
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("", index, name="index"),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('librarian_view/', views.librarian_view, name='librarian_view'),
    path('member_view/', views.member_view, name='member_view'),
    path("add_book/", views.can_add_book_view, name='can_add_book_view'),
    path("edit_book/", views.can_change_book_view, name='can_change_book_view'),
    path("can_delete_book_view/", views.can_delete_book_view, name='can_delete_book_view'),
]