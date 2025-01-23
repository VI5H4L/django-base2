from django.db import models
from .fields import UppercaseCharField

class Product(models.Model):
    name = UppercaseCharField(max_length=100)  # Custom field
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name
