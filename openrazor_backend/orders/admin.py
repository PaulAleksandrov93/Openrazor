from django.contrib import admin
from .models import Order, OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'date_ordered', 'status', 'order_number', 'delivery_address')
    list_filter = ('user', 'date_ordered', 'status')
    search_fields = ('user__username', 'order_number')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'cart_item', 'quantity')
    list_filter = ('order__user', 'order__date_ordered')
    search_fields = ('order__user__username', 'cart_item__product__name')