from django.shortcuts import render
from .serializers import TaskStatusSerializer,ToDoTaskSerializer
from rest_framework  import viewsets
from ToDoApp.models import TaskStatus,ToDoTask
# Create your views here.

class TaskStatusView(viewsets.ModelViewSet):
    queryset = TaskStatus.objects.all()
    serializer_class = TaskStatusSerializer

class ToDoTaskView(viewsets.ModelViewSet):
    queryset = ToDoTask.objects.all()
    serializer_class = ToDoTaskSerializer
