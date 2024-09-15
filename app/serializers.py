from rest_framework import serializers

from .models import Agent, Task, Ticket 


class AgentSerializer(serializers.ModelSerializer):
    """
    Serializer for Agent model"""
    class Meta: # defines how a class should behave
        model = Agent
        fields = ['id','user','name','language_skills','assigned_tasks']
        read_only_fields = ['id']

        def create(self, validated_data):
            agent = Agent.objects.create(**validated_data)
            agent.save()
            return agent


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task model"""
    class Meta:
        model = Task
        fields = ['id','ticket','created_at','updated_at','agent','status','log']
        read_only_fields = ['id']

        def create(self, validated_data):
            task = Task.objects.create(**validated_data)
            task.save()
            return task




class TicketSerializer(serializers.ModelSerializer):
    """
    Serializer for Ticket model"""
    class Meta:
        model = Ticket
        fields = ['id','restriction','platform']
        read_only_fields = ['id']

        def create(self, validated_data):
            ticket = Ticket.objects.create(**validated_data)
            ticket.save()
            return ticket
