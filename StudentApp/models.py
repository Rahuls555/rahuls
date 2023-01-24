from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    section=models.CharField(max_length=10)
    dob=models.DateField()
    class Meta:
        db_table='student'
    
    