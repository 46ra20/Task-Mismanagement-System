from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    Category = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.Category

