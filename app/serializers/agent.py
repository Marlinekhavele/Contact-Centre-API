from rest_framework import serializers

from ..models import Agent

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