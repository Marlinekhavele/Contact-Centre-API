from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.response import Response

from app.models import Ticket
from app.serializers.ticket import TicketSerializer

# Handle Ticket views logic.


class CreateTicketView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def perform_create(self, serializer):
        ticket = serializer.save()
        detail_serializer = TicketSerializer(ticket)
        return Response(detail_serializer.data)


class ListTicketView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ("restriction", "platform")


class RetrieveDestroyUpdateTicketView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    lookup_url_kwarg = "id"
