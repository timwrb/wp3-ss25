from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price_gross = models.FloatField()
    price_net = models.FloatField()

    def __str__(self):
        return self.product_name

# Create your models here.
