from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'image', 'discount', 'on_sale', 'stock_quantity', 'rating', 'date_added', 'tags', 'slug')
    search_fields = ['name', 'category__name']  
