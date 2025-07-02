from rest_framework import serializers
from .models import Stock

class StockSerializer(serializers.Serializer):
    forceInStock = serializers.BooleanField()
    currentStock = serializers.FloatField()
    lowestStock = serializers.FloatField()
    highestStock = serializers.FloatField()

    def create(self, validated_data):
        return Stock.objects.create(**validated_data)

    def update(self, instance: Stock, validated_data):
        instance.forceInStock = validated_data.get("forceInStock", instance.forceInStock)
        instance.currentStock = validated_data.get("currentStock", instance.currentStock)
        instance.lowestStock = validated_data.get("lowestStock", instance.lowestStock)
        instance.highestStock = validated_data.get("highestStock", instance.highestStock)
        instance.save()
        return instance