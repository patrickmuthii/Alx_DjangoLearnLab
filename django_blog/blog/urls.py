from django.urls import path
from django.contrib.auth import views
from django.contrib.auth import views as auth_views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView, CommentDeleteView, CommentUpdateView, search_posts_view


urlpatterns = [

    path('', views.home_view, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('posts/', views.posts_view, name='posts'),  # Ensure 'posts' view exists 
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/comment/new/', CommentCreateView.as_view(), name='new_comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='edit_comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
    path('', views.PostListView.as_view(), name='post_list'),  # List all posts
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),  # Create a new post
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),  # View a single post
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),  # Edit an existing post
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),  # Delete a post
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/comments/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),    
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_edit'),
    path('search/', search_posts_view, name='search_posts'),
    
] 
