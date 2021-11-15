from ToDoApp.views import TaskStatusView,ToDoTaskView
from django.urls import path,include
from rest_framework import routers
from .import views

router = routers.DefaultRouter()
router.register('TaskStatus', views.TaskStatusView)
router.register('ToDoTask', views.ToDoTaskView)


urlpatterns = [
    path('',include(router.urls))
]
