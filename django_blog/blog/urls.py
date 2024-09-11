from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('posts/', views.posts_view, name='posts'),  # Ensure 'posts' view exists
    
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
]