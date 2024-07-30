from django.db import models
from django.core import validators

# Create your models here.


class StudentInfo(models.Model):
    name = models.CharField(max_length=35)
    Mobile_No = models.IntegerField()
    Fee = models.IntegerField()
    Address = models.CharField(max_length=100)