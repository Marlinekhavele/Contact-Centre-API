

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Agent, Task, Ticket

# Create your tests here.

class AgentTests(APITestCase):

    def test_create_agent(self):

        url = reverse('agent-list')
          # Define the data for the new agent
        data = {
            'name': 'John Doe',
            'language_skills': ['English', 'German', 'French'],
            'assigned_tasks': ['Facebook', 'Email']
        }
        
        # Perform the POST request to create the agent
        response = self.client.post(url, data, format='json')
        
        # Assert that the agent was successfully created (status 201)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Verify the agent exists in the database
        self.assertEqual(Agent.objects.count(), 1)
        self.assertEqual(Agent.objects.get().name, 'John Doe')
        self.assertIsNotNone(Agent.objects.get().id)

