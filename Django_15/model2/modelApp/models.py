from django.db import models

class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=70)
    father_name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return f"Name: {self.name}"
