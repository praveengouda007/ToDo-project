from rest_framework import serializers
from .models import TaskStatus, ToDoTask


class TaskStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TaskStatus
        fields = ["status"]

class ToDoTaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDoTask
        fields = '__all__'
