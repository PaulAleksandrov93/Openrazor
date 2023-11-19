from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_order(request):
    """
    Создать новый заказ для авторизованного пользователя на основе его корзины.
    """
    user = request.user

    # Получаем корзину пользователя (предполагаем, что у пользователя есть одна корзина)
    cart = user.cart

    # Создаем новый заказ на основе содержимого корзины
    order = Order.objects.create(user=user, total_price=cart.total_price)

    # Переносим элементы корзины в заказ
    for cart_item in cart.cart_items.all():
        OrderItem.objects.create(order=order, cart_item=cart_item, quantity=cart_item.quantity)

    # Очищаем корзину пользователя
    cart.cart_items.all().delete()

    serializer = OrderSerializer(order)
    return Response(serializer.data, status=201)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_order(request, order_id):
    """
    Обновить детали заказа для авторизованного пользователя.
    Возможно, потребуется, например, для изменения адреса доставки.
    """
    user = request.user
    order = get_object_or_404(Order, id=order_id, user=user)

    # Ваш код для обновления деталей заказа

    serializer = OrderSerializer(order)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_order(request, order_id):
    """
    Получить детали конкретного заказа для авторизованного пользователя.
    """
    user = request.user
    order = get_object_or_404(Order, id=order_id, user=user)

    serializer = OrderSerializer(order)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def cancel_order(request, order_id):
    """
    Отменить заказ для авторизованного пользователя.
    """
    user = request.user
    order = get_object_or_404(Order, id=order_id, user=user)

    # Ваш код для отмены заказа

    return Response('Order canceled successfully!', status=200)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_orders(request):
    """
    Получить историю заказов для авторизованного пользователя.
    """
    user = request.user
    orders = Order.objects.filter(user=user)

    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)