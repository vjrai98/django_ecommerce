from rest_framework import serializers
from .models import (Category,
                     ProductType,
                     ProductSpecification,
                     Product,
                     ProductSpecificationValue,
                     ProductImage)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = "__all__"

