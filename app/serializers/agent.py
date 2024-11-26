from rest_framework import serializers

from ..models import Agent


class AgentSerializer(serializers.ModelSerializer):
    """
    Serializer for Agent model"""

    class Meta:  # defines how a class should behave
        model = Agent
        fields = ["id", "user", "name", "language_skills", "assigned_tasks"]
        read_only_fields = ["id", "user"]

    def validate(self, data):
        user = self.context["request"].user
        if Agent.objects.filter(user=user).exists():
            raise serializers.ValidationError("You already have an agent.")
        return data
