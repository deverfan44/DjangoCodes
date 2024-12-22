from django.db import models
# Create your models here.
class Category(models.Model):
    categroy_name = models.CharField(max_length=100)
    # target = models.ManyToManyField(Task)

    def __str__(self):
        return self.categroy_name

