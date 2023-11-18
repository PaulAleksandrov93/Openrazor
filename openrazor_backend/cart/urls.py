from django.urls import path

from .views import get_cart, add_to_cart, update_cart_item, remove_from_cart

app_name = 'cart'

urlpatterns = [
    path('cart/', get_cart, name='get_cart'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/update/<int:cart_item_id>/', update_cart_item, name='update_cart_item'),
    path('cart/remove/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
]