from django.contrib.auth.models import User
from django.db import models
import uuid
# Create your models here.

class Agent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='agent_profile')
    name = models.CharField(max_length=100)
    language_skills = models.JSONField() 
    assigned_tasks = models.JSONField(default=list)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    agent = models.ForeignKey('Agent', on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    log = models.JSONField(default=list)

    def __str__(self):
        return self.status

class Ticket(models.Model):
    PLATFORM_CHOICES = [
        ('facebook_chat', 'Facebook Chat'),
        ('email', 'Email'),
        ('call', 'Call'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    restriction = models.JSONField(default=list)
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    def __str__(self):
        return self.restriction