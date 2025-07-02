from django.db import models
from productmanager.models import Product

class Stock(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    forceInStock = models.BooleanField(default=False)
    currentStock = models.FloatField(default=0.0)
    lowestStock = models.FloatField(default=0.0)
    highestStock = models.FloatField(default=0.0)

    def __str__(self):
        return f"Stock for {self.product.name}"