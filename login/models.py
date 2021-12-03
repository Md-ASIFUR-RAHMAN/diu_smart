from django.db import models

# Create your models here.
class person_performance_details(models.Model):
    name = models.CharField(max_length=20)
    availability_in_percentage = models.IntegerField()
    performance_in_percentage = models.IntegerField()
    task = models.CharField(max_length=50)
    work_activity = models.CharField(max_length=10)

class performance_details(models.Model):
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=30)
    date = models.DateField()
    availability_in_percentage = models.IntegerField()
    performance_in_percentage = models.IntegerField()
    task = models.CharField(max_length=50)
    work_activity = models.CharField(max_length=10)