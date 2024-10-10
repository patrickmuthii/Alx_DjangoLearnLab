from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from .models import Task, CustomUser

class TaskAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = CustomUser.objects.create_user(
            username='patrick', 
            email='murimipatrick101@gmail.com', 
            password='123456789'
        )

        # Create a client and forces to authenticate the user
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        # URL for task list and creation
        self.task_url = reverse('task-list-create')  # Adjust according to your URL names
    
    def test_create_task(self):
        # Test task creation
        task_data = {
            'title': 'finish project',
            'description': 'finish the project on time',
            'due_date': '2024-10-18',
            'priority': 'High',
            'status': 'Incomplete'
        }
        
        response = self.client.post(self.task_url, task_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'finish project')

    def test_get_task_list(self):
        # Create a sample task
        Task.objects.create(
            title='visit the hub',
            description='visit the hub at noon',
            due_date='2024-10-15',
            priority='Medium',
            status='Incomplete',
            user=self.user
        )
        
        # Test retrieving the task list
        response = self.client.get(self.task_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'visit the hub')

    def test_update_task(self):
        # Create a task to update
        task = Task.objects.create(
            title='make coffee',
            description='make coffee at the morning',
            due_date='2024-10-15',
            priority='Low',
            status='In Progress',
            user=self.user
        )
        
        # Task detail URL
        task_detail_url = reverse('task-detail', kwargs={'pk': task.id})
        
        # Update data
        updated_data = {
            'title': 'do research',
            'description': 'do research for the project',
            'due_date': '2024-12-31',
            'priority': 'High',
            'status': 'Complete'
        }
        
        response = self.client.put(task_detail_url, updated_data, format='json')
        
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task.refresh_from_db()
        self.assertEqual(task.title, 'do research')
        self.assertEqual(task.status, 'Complete')

    def test_delete_task(self):
        # Create a task to delete
        task = Task.objects.create(
            title='Take a walk',
            description='Take a walk at the morning',
            due_date='2024-12-31',
            priority='Low',
            status='pending',
            user=self.user
        )
        
        # Task detail URL
        task_detail_url = reverse('task-detail', kwargs={'pk': task.id})
        
        response = self.client.delete(task_detail_url)
        
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
