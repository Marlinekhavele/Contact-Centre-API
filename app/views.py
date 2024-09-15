
from rest_framework import generics
from rest_framework.response import Response
from django_filters import rest_framework as filters
from app.models import Agent, Task, Ticket
from app.serializers import AgentSerializer, TaskSerializer, TicketSerializer 

# Create your views here.


class CreateAgentView(generics.CreateAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

    def perform_create(self, serializer):
        order = serializer.save()
        detail_serializer = AgentSerializer(order)
        return Response(detail_serializer.data)

class ListAgentView(generics.ListAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('user__id', 'name')


class RetrieveDestroyUpdateAgentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    lookup_url_kwarg = 'id'
