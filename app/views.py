
from rest_framework.viewsets import ModelViewSet
from app.models import Agent, Task, Ticket
from app.serializers import AgentSerializer, TaskSerializer, TicketSerializer 

# Create your views here.
class AgentViewSet(ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer