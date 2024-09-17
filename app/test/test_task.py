from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from app.models import Task
class TaskTests(APITestCase):
    def setUp(self):
        self.agent = Agent.objects.create(name='Marline', language_skills='en')
        self.task = Task.objects.create(ticket_id=self.ticket.id, agent_id=self.agent.id, status='In progress')
        self.data = {'ticket_id': self.ticket.id, 'agent_id': self.agent.id, 'status': 'In progress'}
       

    def test_task_creation(self):
        url = reverse('create-task')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)  
        self.assertEqual(Task.objects.latest('id').status, 'In progress')

    def test_task_list(self):
        url = reverse('tasks-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    def test_task_retrieve(self):
        url = reverse('tasks-get-delete-update', kwargs={'id': self.task.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], self.task.status)

        data = {
            'ticket_id': 1,
            'agent_id': 1,
            'status': 'In progress'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().status, 'In progress')
