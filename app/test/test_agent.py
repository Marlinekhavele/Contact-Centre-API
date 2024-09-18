from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from app.models import Agent

class AgentTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.agent_data = {
            'name': 'Test Agent',
            'language_skills': ['English', 'German'],
            'assigned_tasks': []
        }

    def test_create_agent(self):
        url = reverse('create-agent')
        response = self.client.post(url, self.agent_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Agent.objects.count(), 1)
        self.assertEqual(Agent.objects.get().name, 'Test Agent')

        # create a second agent for the same user
        response = self.client.post(url, {'name': 'Second Agent'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Agent.objects.count(), 1)

    def test_list_agents(self):
        Agent.objects.create(user=self.user, **self.agent_data)
        url = reverse('agents-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_unauthenticated_access(self):
        self.client.credentials()
        url = reverse('agents-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthorized_access(self):
        other_user = User.objects.create_user(username='otheruser', password='otherpass123')
        other_agent = Agent.objects.create(user=other_user, name='Other Agent')
        url = reverse('agents-get-delete-update', kwargs={'id': other_agent.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    