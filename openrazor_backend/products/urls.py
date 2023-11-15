from django.urls import path
from .views import getProducts, getProduct, createProduct, updateProduct, deleteProduct

app_name = 'products'

urlpatterns = [
    path('products/', getProducts, name='getProducts'),
    path('products/<int:pk>/', getProduct, name='getProduct'),
    path('products/create/', createProduct, name='createProduct'),
    path('products/update/<int:pk>/', updateProduct, name='updateProduct'),
    path('products/delete/<int:pk>/', deleteProduct, name='deleteProduct'),
]