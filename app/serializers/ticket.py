from rest_framework import serializers

from ..models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    """
    Serializer for Ticket model"""

    class Meta:
        model = Ticket
        fields = ["id", "restriction", "platform", "priority"]
        read_only_fields = ["id"]

        def create(self, validated_data):
            ticket = Ticket.objects.create(**validated_data)
            ticket.save()
            return ticket
