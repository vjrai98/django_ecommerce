from django.urls import path, include
from .views import ProductView,ProductTypeView,CategoryView

urlpatterns = [
    path('products/', ProductView.as_view(), name='products'),
    path('prodtype/', ProductTypeView.as_view(), name='product-type'),
    path('prodcat/', CategoryView.as_view(), name='category'),
]
