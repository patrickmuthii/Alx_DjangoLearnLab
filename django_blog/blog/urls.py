from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import post_detail_view, edit_comment_view, delete_comment_view


urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('posts/', views.posts_view, name='posts'),  # Ensure 'posts' view exists 
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('post/<int:pk>/', post_detail_view, name='post_detail'),
    path('comment/<int:pk>/edit/', edit_comment_view, name='edit_comment'),
    path('comment/<int:pk>/delete/', delete_comment_view, name='delete_comment')
    path('', views.PostListView.as_view(), name='post_list'),  # List all posts
    path('posts/new/', views.PostCreateView.as_view(), name='post_create'),  # Create a new post
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),  # View a single post
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),  # Edit an existing post
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),  # Delete a post
    path('', views.PostListView.as_view(), name='post_list'),
    path('posts/new/', views.PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),    


]    
