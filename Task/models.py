from django.db import models
from category.models import CategoryModel

# Create your models here.

class TaskModels(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    taskAssignDate = models.DateField(auto_now_add=True)
    Category  = models.ManyToManyField(CategoryModel)
    

    def __str__(self) -> str:
        return self.taskTitle
