from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('posts/', views.posts_view, name='posts'),  # Ensure 'posts' view exists
    
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
]