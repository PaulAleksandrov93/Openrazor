from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Cart, CartItem
from products.models import Product

class CartTests(TestCase):
    def setUp(self):
        # Создаем пользователя для тестирования
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Создаем продукт для тестирования
        self.product = Product.objects.create(name='Test Product', description='Description', price=10.99)

        # Создаем клиента API
        self.client = APIClient()

    def test_get_cart(self):
        # Авторизуем пользователя
        self.client.force_authenticate(user=self.user)

        # Создаем корзину для пользователя
        Cart.objects.create(user=self.user.userprofile)

        # Выполняем GET-запрос для получения корзины
        response = self.client.get('/api/cart/')

        # Проверяем успешность запроса
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверяем, что в ответе есть ожидаемые данные
        self.assertIn('total_price', response.data)

    def test_add_to_cart(self):
        # Выполняем POST-запрос для добавления продукта в корзину
        response = self.client.post(f'/api/cart/add/{self.product.id}/')

        # Проверяем успешность запроса
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Проверяем, что в ответе есть ожидаемые данные
        self.assertIn('quantity', response.data)

    def test_update_cart_item(self):
        # Создаем корзину для пользователя
        cart = Cart.objects.create(user=self.user.userprofile)

        # Создаем элемент корзины
        cart_item = CartItem.objects.create(cart=cart, product=self.product, quantity=1)

        # Выполняем PUT-запрос для обновления элемента корзины
        data = {'quantity': 2}
        response = self.client.put(f'/api/cart/update/{cart_item.id}/', data)

        # Проверяем успешность запроса
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверяем, что в ответе есть ожидаемые данные
        self.assertEqual(response.data['quantity'], 2)

    def test_remove_from_cart(self):
        # Создаем корзину для пользователя
        cart = Cart.objects.create(user=self.user.userprofile)

        # Создаем элемент корзины
        cart_item = CartItem.objects.create(cart=cart, product=self.product, quantity=1)

        # Выполняем DELETE-запрос для удаления элемента корзины
        response = self.client.delete(f'/api/cart/remove/{cart_item.id}/')

        # Проверяем успешность запроса
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Проверяем, что элемент корзины был удален
        self.assertFalse(CartItem.objects.filter(id=cart_item.id).exists())