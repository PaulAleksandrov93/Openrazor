from django.urls import path
from .views import create_order, update_order, get_order, cancel_order, get_user_orders

app_name = 'orders'

urlpatterns = [
    path('create/', create_order, name='create_order'),
    path('<int:order_id>/', get_order, name='get_order'),
    path('<int:order_id>/cancel/', cancel_order, name='cancel_order'),
    path('<int:order_id>/update/', update_order, name='update_order'),
    path('user/', get_user_orders, name='get_user_orders'),
]