from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from app.models import Agent

class AgentTests(APITestCase):
    def setUp(self):
        self.agent = Agent.objects.create(name='Marline', language_skills='en')
        self.data = {'name': 'Marline', 'language_skills': 'en'}

    def test_agent_creation(self):
        url = reverse('create-agent')
        data = {
            'name': 'Marline',
            'language_skills': 'en'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Agent.objects.count(), 1)
        self.assertEqual(Agent.objects.get().name, 'Marline')

    def test_agent_list(self):
        url = reverse('list-agent')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
