#from asyncio import tasks
#from .forms import TaskForm 
#from typing import Self
from django.http import request
from django.shortcuts import render, redirect
from rest_framework import generics, permissions 
from .serializers import TaskSerializer, UserSerializer
from django.shortcuts import get_object_or_404 
from .models import Task
from rest_framework.permissions import IsAuthenticated
from Task import serializers 
from django.contrib import messages

# Create your views here.


class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


    
def update_task(request, pk):
        task = get_object_or_404(Task, pk=pk)

        if task.status == 'Completed':
            messages.error(request, 'You can not edit this task because you have already completed this task. Please mark it as incomplete first to edit.')
            return render(request, 'task/task_update.html', {'task': task})
        if request.method == 'POST':
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()

                notification_mail(request.user, task)
                return redirect('task-list')
        
        else:
            form = TaskForm(instance=task)
        return render(request, 'task/task_form.html', {'form': form})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete() 
        return redirect('task-list')
    return render(request, 'task/task_delete.html', {'task': task})



def task_list(request):
    tasks = Task.objects.all()  
    return render(request, 'task/task_list.html', {'tasks': tasks})


from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required



#  
@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user # Assign the current logged-in user to the task
            task.save()
            # Send email notification after task creation
            notification_mail(request.user, task)
            return redirect('task-list')  # Redirect to the task list view after saving
    else:
        form = TaskForm()
    return render(request, 'task/task_create.html', {'form': form})

from django.core.mail import send_mail
from django.conf import settings
from .models import Task
from datetime import timedelta
from django.utils import timezone

# Send email notification after task creation for reminder about the task
def notification_mail(user, task):
    subject = f"Task Update: {task.title}"
    message = f"Dear {user.username},\n\nYour task '{task.title}' has been updated.\n\nDetails:\nTitle: {task.title}\nDescription: {task.description}\nDue Date: {task.due_date}\nPriority: {task.get_priority_display()}\nStatus: {task.get_status_display()}\n\nThank you!"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email]

    send_mail(subject, message, from_email, recipient_list)


def create_recurring_task(task):
    if task.recurrence == 'Daily':
        new_due_date = task.due_date + timedelta(days=1)
    elif task.recurrence == 'Weekly':
        new_due_date = task.due_date + timedelta(weeks=1)
    elif task.recurrence == 'Monthly':
        due_date = task.due_date + timedelta(days=30)
    else:
        due_date = None

    Task.objects.create(
        title=task.title,
        description=task.description,
        due_date=due_date,
        user=task.user,
        priority=task.priority,
        status=task.status,
        recurrence=task.recurrence
    )
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.status = 'Completed'
    task.save()
    return redirect('task-list')
