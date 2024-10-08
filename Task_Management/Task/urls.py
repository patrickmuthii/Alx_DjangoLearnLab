from django.urls import path
from .views import TaskListCreateView, TaskDetailView 
from django.contrib.auth import views as auth_views
from . import views

#urls for Task Management API
urlpatterns = [
    path('api/login/', auth_views.LoginView.as_view(), name='login'),
    path('api/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('task/', TaskListCreateView.as_view(), name = 'task-list-create'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name = 'task-detail'),
    path('', views.task_list, name = 'task-list'),
    path('task/create/', views.task_create, name = 'task-create'),
    
    path('notifications/', views.notification_mail, name='notification_list'),
    path('task/<int:pk>/complete/', views.complete_task, name = 'complete-task'),
    path('task/<int:pk>/delete/', views.delete_task, name = 'delete-task'),
    path('task/<int:pk>/update/', views.update_task, name = 'update-task'),
    path('task/<int:pk>/recurring/', views.create_recurring_task, name = 'create-recurring-task'),
]