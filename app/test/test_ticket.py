from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from app.models import Ticket


class TicketTests(APITestCase):
    def setUp(self):
        self.ticket_data = {"platform": "call", "restriction": "English", "priority": 0}
        self.ticket = Ticket.objects.create(**self.ticket_data)

    def test_create_ticket(self):
        url = reverse("create-ticket")
        response = self.client.post(url, self.ticket_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ticket.objects.count(), 2)
        self.assertEqual(Ticket.objects.last().platform, "call")
