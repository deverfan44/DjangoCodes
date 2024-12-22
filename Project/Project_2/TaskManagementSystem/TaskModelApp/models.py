from django.db import models
from TaskCategoryApp.models import Category
# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    assign_date = models.DateField()
    relation = models.ManyToManyField(to=Category)

    def __str__(self):
        return self.name