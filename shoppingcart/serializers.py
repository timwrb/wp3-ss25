from django.contrib.auth.models import User
from rest_framework import serializers

from adressmanager.models import adresses
from adressmanager.serializers import AdressSerializer
from shoppingcart.models import Customer


class CustomerSerializers(serializers.Serializer):
    salutation =  serializers.CharField(max_length=5)
    birthdate = serializers.DateField()
    adresses = AdressSerializer(many=True, required=False)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def create(self, validated_data):
        addresses_data = validated_data.pop('addresses', [])
        customer = Customer.objects.create(**validated_data)

        for address_data in addresses_data:
            adresses.objects.create(customer=customer, **address_data)

        return customer
