from django.urls import path
from .views import RegisterView, CustomLoginView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
