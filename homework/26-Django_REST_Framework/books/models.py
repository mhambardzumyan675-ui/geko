from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    description=models.TextField(max_length=100)
    pages=models.PositiveIntegerField()
    price=models.DecimalField(max_digits=7,decimal_places=2)
    is_available=models.BooleanField(default=True)
    created_at=models.DateField(auto_now_add=True)

def __str__(self):
    return self.title