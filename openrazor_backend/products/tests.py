from django.test import TestCase
from rest_framework.test import APIClient
from .models import Product, Category
from django.urls import reverse
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile

class ProductTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category_data = {'name': 'Test Category'}  
        self.category = Category.objects.create(**self.category_data)

        self.product_data = {
            'name': 'Test Product',
            'description': 'This is a test product.',
            'price': 19.99,
            'category': self.category.id,
            'discount': 5.0,
            'on_sale': True,
            'stock_quantity': 50,
            'rating': 4.5,
            'tags': 'tag1, tag2',
        }
        self.product = Product.objects.create(**self.product_data)

    def test_create_product(self):
        """
        Тест на создание нового продукта.
        """
        url = reverse('products:create_product')
        response = self.client.post(url, self.product_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)  # Проверяем, что количество продуктов увеличилось.

    def test_get_product_list(self):
        """
        Тест на получение списка продуктов.
        """
        url = reverse('products:get_products')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Проверяем, что в ответе только один продукт.

    def test_get_single_product(self):
        """
        Тест на получение информации о конкретном продукте.
        """
        url = reverse('products:get_product', kwargs={'pk': self.product.id})
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product_data['name'])

    def test_update_product(self):
        """
        Тест на обновление информации о продукте.
        """
        updated_data = {'name': 'Updated Product Name', 'price': 25.0}
        url = reverse('products:update_product', kwargs={'pk': self.product.id})
        response = self.client.put(url, updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.get(id=self.product.id).name, updated_data['name'])

    def test_delete_product(self):
        """
        Тест на удаление продукта.
        """
        url = reverse('products:delete_product', kwargs={'pk': self.product.id})
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)  # Проверяем, что продукт был удален.
