from django.db import models

# Create your models here.
class Student(models.Model):
    name =models.CharField(max_length=30)
    roll_no =models.IntegerField()
    department =models.CharField(max_length=20)
    email =models.EmailField()
    marks =models.IntegerField()
