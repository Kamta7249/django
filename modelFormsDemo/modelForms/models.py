from django.db import models

# Create your models here.

class Project(models.Model):
    startDate = models.DateField()
    endDate = models.DateField()
    name = models.CharField(max_length=25)
    assignedTo = models.CharField(max_length=30)
    priority = models.IntegerField()
