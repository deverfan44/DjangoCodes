from django.db import models
from musicianApp.models import musicianModel
# Create your models here.

rating = (("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")) 
class albumModel(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(musicianModel, on_delete=models.CASCADE)
    release_date = models.DateField()
    rating = models.CharField(max_length=20, choices=rating, default='3') # Helo from geeksforgeeks

    def __str__(self):
        return f"Name: {self.name} and Authon: {self.author.first_name}"