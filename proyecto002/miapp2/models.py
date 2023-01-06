from django.db import models

# Create your models here.

class Curso(models.Model):
    code=models.CharField(max_length=8)
    name= models.CharField(max_length=20)
    hour= models.CharField(max_length=5)
    credits= models.CharField(max_length=10)
    state= models.CharField(max_length=10)
