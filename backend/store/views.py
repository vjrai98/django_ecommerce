from django.shortcuts import render
from rest_framework import generics
from .models import (Category,
                     ProductType,
                     ProductSpecification,
                     Product,
                     ProductSpecificationValue,
                     ProductImage)
from .serializers import (
    ProductTypeSerializer, ProductSerializer,
    CategorySerializer)


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductTypeView(generics.ListCreateAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
