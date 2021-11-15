from django.contrib import admin
from .models import TaskStatus, ToDoTask
# Register your models here.
admin.site.register(TaskStatus)
admin.site.register(ToDoTask)
