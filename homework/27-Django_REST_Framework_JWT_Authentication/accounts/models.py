from django.db import models

class User(models.Model):
      email=models.EmailField(unique=True)
      bio=models.TextField(max_length=100)
      

