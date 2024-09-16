from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from app.models import Task

class TaskTests(APITestCase):
    def setUp(self):
        pass