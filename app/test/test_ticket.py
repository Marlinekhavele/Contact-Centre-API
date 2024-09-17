from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from app.models import Ticket

class TicketTests(APITestCase):
    def setUp(self):
        self.valid_payload = {
            'restriction': ['en'],
            'platform': 'email'
        }

    def test_ticket_creation(self):
        url = reverse('tickets-list')
        response = self.client.post(url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ticket.objects.count(), 1)
        self.assertEqual(Ticket.objects.get().platform, 'email')
