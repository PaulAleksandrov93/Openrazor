from django.db.models.signals import post_save
from django.dispatch import receiver
from cart.models import Cart
from orders.models import Order

@receiver(post_save, sender=Order)
def clear_cart(sender, instance, **kwargs):
    # Очистка связанной корзины после создания заказа
    if kwargs['created']:
        if instance.user:
            # Если заказ связан с пользователем, очищаем корзину пользователя
            user_cart = Cart.objects.filter(user=instance.user)
        else:
            # Иначе (если заказ анонимный), очищаем корзину по сессии
            user_cart = Cart.objects.filter(session_id=instance.items.first().cart.session.session_key)
        
        user_cart.delete()