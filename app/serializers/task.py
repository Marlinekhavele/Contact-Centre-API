from rest_framework import serializers

from ..models import  Task
from ..tasks import assign_task

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task model"""
    class Meta:
        model = Task
        fields = ['id','ticket','created_at','updated_at','agent','status','log']
        read_only_fields = ['id']

        def create(self, validated_data):
            task = Task.objects.create(**validated_data)
            assign_task.delay(str(task.id))  # Trigger asynchronous assignment

            task.save()
            return task
