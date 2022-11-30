from products.models import Category, Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product model
    """
    
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = [
            'id',
            'category',
            'title',
            'description',
            'image',
            'slug',
            'price',
            'in_stock',
            'is_active',
            'created',
            'updated',
        ]
        read_only = True
        editable = False
