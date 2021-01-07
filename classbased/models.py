from django.db import models
from django.urls import reverse

# Create your models here.

class Student(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=40)
    sage=models.IntegerField()
    scity=models.CharField(max_length=50)

    def get_absolute_url(request):
        return reverse("hello")
