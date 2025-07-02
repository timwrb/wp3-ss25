from rest_framework import serializers

from cart.models import Cart, Entry
from productmanager.serializers import ProductSerializer

class EntrySerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    product_name = serializers.CharField(max_length=50)
    net = serializers.FloatField()
    gross = serializers.FloatField()
    total_net = serializers.FloatField()
    total_gross = serializers.FloatField()
    quantity = serializers.IntegerField()

    def create(self, validated_data):
        return Entry.objects.create(**validated_data)


class CartSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    customer_id = serializers.IntegerField(required=False)
    net = serializers.FloatField()
    gross = serializers.FloatField()
    tax_value = serializers.FloatField()
    entries = EntrySerializer(many=True)

    def create(self, validated_data):
        return Cart.objects.create(**validated_data)

    def update(self, instance:Cart, validated_data):
        instance.net = validated_data.get("netto")
        instance.gross = validated_data.get("brutto")
        instance.tax_value = validated_data.get("steueranteil")
        instance.entries = validated_data.get("entries")
        instance.save()
        return instance

class AddToCartSerializer(serializers.Serializer):
    cart_id = serializers.IntegerField(required=False)
    product_id = serializers.IntegerField(required=True)
    quantity = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return Entry.objects.create(**validated_data)
