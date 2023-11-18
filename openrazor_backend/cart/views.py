from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from django.shortcuts import get_object_or_404
from products.models import Product  

@api_view(['GET'])
def get_cart(request):
    user = request.user
    if user.is_authenticated:
        # Если пользователь авторизован, получаем корзину по его профилю
        cart, created = Cart.objects.get_or_create(user_profile=user.userprofile)
    else:
        # Иначе получаем корзину из сессии
        cart, created = Cart.objects.get_or_create(session_id=request.session.session_key)

    serializer = CartSerializer(cart)
    return Response(serializer.data)

@api_view(['POST'])
def add_to_cart(request, product_id):
    user = request.user
    if user.is_authenticated:
        # Если пользователь авторизован, получаем корзину по его профилю
        cart, created = Cart.objects.get_or_create(user_profile=user.userprofile)
    else:
        # Иначе получаем корзину из сессии
        cart, created = Cart.objects.get_or_create(session_id=request.session.session_key)

    product = get_object_or_404(Product, id=product_id)
    
    serializer = CartItemSerializer(data={'cart': cart.id, 'product': product.id, 'quantity': 1})
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_cart_item(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    serializer = CartItemSerializer(instance=cart_item, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return Response('Товар успешно удален из корзины!', status=204)