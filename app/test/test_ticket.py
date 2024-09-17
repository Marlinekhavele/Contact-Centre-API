from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from app.models import Ticket

class TicketTests(APITestCase):
    def setUp(self):
        self.ticket = Ticket.objects.create(restriction='None', platform='Facebook', priority=0)
        self.data = {'restriction': 'None', 'platform': 'Facebook', 'priority': 0}

    def test_ticket_creation(self):
        url = reverse('create-ticket') 
        data = {
            'restriction': 'None',
            'platform': 'Facebook',
            'priority': 0
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ticket.objects.count(), 1)
        self.assertEqual(Ticket.objects.get().platform, 'Facebook')

    def test_ticket_list(self):
        url = reverse('tickets-list') 
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_ticket_retrieve(self):
        url = reverse('tickets-get-delete-update', kwargs={'id': self.ticket.id}) 
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['platform'], self.ticket.platform)
