from rest_framework import serializers

from ..models import  Task

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task model"""
    class Meta:
        model = Task
        fields = ['id','ticket','created_at','updated_at','agent','status']
        read_only_fields = ['id']

        def create(self, validated_data):
            task = Task.objects.create(**validated_data)
            task.save()
            return task
