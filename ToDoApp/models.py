from django.db import models

# Create your models here.
class TaskStatus(models.Model):
    status = models.CharField(max_length= 20)

    def __str__(self):
        return self.status

class ToDoTask(models.Model):
    Status = models.ForeignKey(TaskStatus,on_delete=models.CASCADE)
    Task = models.CharField(max_length = 100)
    created_by = models.CharField(max_length = 20)
    time = models.TimeField()

    def __str__(self):
        return "%s %s %s %s" % (self.created_by,self.Task,self.Status,self.time)
