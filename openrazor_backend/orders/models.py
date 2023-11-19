from django.db import models
from django.contrib.auth.models import User
from cart.models import CartItem
from django.utils.crypto import get_random_string
from datetime import datetime

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, default='в обработке')
    order_number = models.CharField(max_length=255, unique=True)
    delivery_address = models.CharField(max_length=255, default='')  # Добавлено поле для адреса доставки

    def save(self, *args, **kwargs):
        # Генерация уникального номера заказа перед сохранением
        if not self.order_number:
            self.order_number = generate_unique_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.order_number} - User: {self.user.username}, Status: {self.status}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    cart_item = models.OneToOneField(CartItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Обновляем общую стоимость заказа при сохранении OrderItem
        self.order.total_price += self.cart_item.total_price
        self.order.save()

    def __str__(self):
        return f"OrderItem {self.id} - Order: {self.order.order_number}, Product: {self.cart_item.product.name}, Quantity: {self.quantity}"

def generate_unique_order_number():
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    random_string = get_random_string(length=6)
    return f"{timestamp}-{random_string}"