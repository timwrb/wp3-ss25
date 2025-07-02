from django.db import models

from shoppingcart.models import Customer

# Create your models here.

class adresses(models.Model):
    anrede = models.CharField(max_length=5)
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    street = models.CharField(max_length=30)
    house_number = models.CharField(max_length=5)
    postal_code = models.IntegerField()
    city = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="adresses")

    def __str__(self):
        return (f"Anrede: {self.anrede}"
                f"Vorname: {self.firstname}"
                f"Nachname: {self.lastname}"
                f"Straße: {self.street}"
                f"Hausnummer: {self.house_number}"
                f"Postleitzahl: {self.postal_code}"
                f"Ort: {self.city}"
                f"Customer ID: {self.customer}")