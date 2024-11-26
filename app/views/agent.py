from django_filters import rest_framework as filters
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.models import Agent
from app.serializers.agent import AgentSerializer


# we handle Agent views.
class CreateAgentView(generics.CreateAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        agent = serializer.save(user=self.request.user)
        return Response(AgentSerializer(agent).data, status=status.HTTP_201_CREATED)


class ListAgentView(generics.ListAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = "name"

    # Enforce authentication
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return only the agents associated with the current authenticated user
        return Agent.objects.filter(user=self.request.user)


class RetrieveDestroyUpdateAgentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "id"

    def get_queryset(self):
        return Agent.objects.filter(user=self.request.user)
