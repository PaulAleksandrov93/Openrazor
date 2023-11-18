from django.db import models
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from products.models import Product

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, null=True, blank=True, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Cart {self.id} - User: {self.user.username if self.user else 'Anonymous'}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"CartItem {self.id} - {self.product.name} ({self.quantity} units)"