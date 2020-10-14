from django.db import models

# Create your models here.
class Week(models.Model):
    week = models.CharField(max_length=100)
    year = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')