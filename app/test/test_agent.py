from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from app.models import Agent

class AgentTests(APITestCase):
    def setUp(self):
        # Create and log in a user
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        
        # Create an agent with the user field set
        self.agent = Agent.objects.create(name='Marline', language_skills='en', user=self.user)

    def test_agent_creation(self):
        url = reverse('create-agent')
        data = {
            'name': 'Marline', 
            'language_skills': 'en',
            'user': self.user.id  # Ensure user field is included
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Agent.objects.count(), 2)  # One from setup, one created
        self.assertEqual(Agent.objects.latest('id').name, 'Marline')

    def test_agent_list(self):
        url = reverse('agents-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  

