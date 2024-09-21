from django.urls import path
from .views import RegisterView, LoginView, FollowUserView, UnfollowUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('follow/<str:username>/', FollowUserView.as_view(), name='follow'),
    path('unfollow/<str:username>/', UnfollowUserView.as_view(), name='unfollow'),
]
