from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    father_name = models.CharField(max_length=100,default='Mr', null= True)
    mother_name = models.CharField(max_length=100,default='Mrs')

    def __str__(self):
        return f"Name: {self.name} Roll: {self.roll}"
    
class Employee(models.Model):
    emp_id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=90)
    age = models.IntegerField()

    def __str__(self):
        return f"Name: {self.name}"