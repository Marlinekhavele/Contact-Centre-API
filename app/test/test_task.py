from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from app.models import Agent, Task, Ticket
from rest_framework.authtoken.models import Token

class TaskTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.agent = Agent.objects.create(name='Test Agent', language_skills=['en'], user=self.user)
        self.ticket = Ticket.objects.create(restriction=['en'], platform='email')
        self.task = Task.objects.create(ticket=self.ticket, agent=self.agent, status='in_progress')

    def test_task_creation(self):
        url = reverse('tasks-list')
        data = {
            'ticket': self.ticket.id,
            'agent': self.agent.id,
            'status': 'open'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_task_list(self):
        url = reverse('tasks-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_task_retrieve(self):
        url = reverse('tickets-get-delete-update', args=[self.task.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], str(self.task.id))