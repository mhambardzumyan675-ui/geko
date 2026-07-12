from django.db import models

# Create your models here.

class Products(models.Model):
    name=models.CharField(max_length=10)
    price=models.PositiveIntegerField()
    desc=models.TextField(max_length=50)