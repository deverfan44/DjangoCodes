from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"Name: {self.name}"

