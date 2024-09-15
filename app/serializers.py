from rest_framework import serializers

from .models import Agent, Task, Ticket 


class AgentSerializer(serializers.ModelSerializer):
    """
    Serializer for Agent model"""
    class Meta: # defines how a class should behave
        model = Agent
        fields = "__all__"

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task model"""
    class Meta:
        model = Task
        fields = "__all__"



class TicketSerializer(serializers.ModelSerializer):
    """
    Serializer for Ticket model"""
    class Meta:
        model = Ticket
        fields = "__all__"
