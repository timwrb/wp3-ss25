from django.db import models

# Create your models here.

class products(models.Model):
    product_name = models.CharField(max_length=50)
    priceB = models.FloatField()
    priceN = models.FloatField()

    
    