from rest_framework import serializers
from .models import Product
from decimal import Decimal, ROUND_HALF_UP

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10,decimal_places=2, source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self,product:Product):
        return  (product.unit_price * Decimal(1.1)).quantize(Decimal("0.01"),rounding=ROUND_HALF_UP)
    
