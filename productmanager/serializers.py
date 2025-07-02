from rest_framework import serializers

from productmanager.models import Product


class ProductSerializer(serializers.Serializer):
    product_name = serializers.CharField(max_length=100)
    price_gross = serializers.DecimalField(max_digits=10, decimal_places=2)
    price_net = serializers.DecimalField(max_digits=10, decimal_places=2)
    id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance:Product, validated_data):
        instance.product_name = validated_data.get("name")
        instance.product_number = validated_data.get("product_number")
        instance.price_gross = validated_data.get("price_brutto")
        instance.price_gross = validated_data.get("price_netto")
        instance.save()
        return instance
