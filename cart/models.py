from django.db import models

from shoppingcart.models import Customer
from productmanager.models import Product


class Cart(models.Model):
    net = models.FloatField(null=True, default=0)
    gross = models.FloatField(null=True, default=0)
    tax_value = models.FloatField(null=True, default=0)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return (
            f"Nettowert: {self.net}    "
            f"Bruttowert: {self.gross}   "
            f"Steueranteil: {self.tax_value}   "
        )


class Entry(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=50)
    net = models.FloatField()
    gross = models.FloatField()
    total_net = models.FloatField()
    total_gross = models.FloatField()
    quantity = models.IntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="entries")

    def __str__(self):
        return (
            f"ProduktId: {self.product_id}   "
            f"Produktname: {self.product_name}   "
            f"Nettopreis/Stk: {self.net}   "
            f"Bruttopreis/Stk: {self.gross}   "
            f"Nettopreis/Gesamt: {self.total_net}   "
            f"Bruttopreis/Gesamt: {self.total_gross}   "
            f"Anzahl: {self.quantity}   "
        )

