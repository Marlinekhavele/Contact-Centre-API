from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.response import Response

from app.models import Task
from app.serializers.task import TaskSerializer

from ..tasks import assign_task


# Handle Task views logic.
class CreateTaskView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        task = serializer.save()
        assign_task.delay(str(task.id))  # Trigger asynchronous assignment
        detail_serializer = TaskSerializer(task)
        return Response(detail_serializer.data)


class ListTaskView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ("ticket__id", "created_at")


class RetrieveDestroyUpdateTaskView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_url_kwarg = "id"
