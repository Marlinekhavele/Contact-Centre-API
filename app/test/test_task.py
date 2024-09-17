from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from app.models import Agent, Task, Ticket

def setUp(self):
    self.user = User.objects.create_user(username='testuser', password='testpass123')
    self.agent = Agent.objects.create(user=self.user, name='Test Agent', language_skills=['English', 'German'], assigned_tasks=[])
    self.ticket = Ticket.objects.create(platform='call', restriction='English', priority=0)
    self.task_data = {
        'ticket': self.ticket.id,
        'agent': self.agent.id,
        'status': 'In progress'
    }

def test_create_task(self):
    url = reverse('create-task')
    self.client.force_authenticate(user=self.user)  # Add authentication
    response = self.client.post(url, self.task_data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Task.objects.count(), 1)
    created_task = Task.objects.first()
    self.assertEqual(created_task.status, 'In progress')
    self.assertEqual(created_task.ticket, self.ticket)
    self.assertEqual(created_task.agent, self.agent)

def test_list_tasks(self):
    Task.objects.create(**self.task_data)
    url = reverse('tasks-list')
    self.client.force_authenticate(user=self.user)  # Add authentication
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)



      