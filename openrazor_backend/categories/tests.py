from django.test import TestCase

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Category

class CategoryTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category_data = {
            'name': 'Test Category',
            'description': 'This is a test category.',
            'is_featured': True,
            'tags': 'tag1, tag2',
            'slug': 'test-category',
        }
        self.category = Category.objects.create(**self.category_data)
        self.url = reverse('categories:category-list')

    def test_create_category(self):
        response = self.client.post(self.url, self.category_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)  # Assuming there's already one category in the database

    def test_retrieve_category_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.category.name)
        self.assertEqual(response.data[0]['description'], self.category.description)
        self.assertEqual(response.data[0]['is_featured'], self.category.is_featured)
        self.assertEqual(response.data[0]['tags'], self.category.tags)
        self.assertEqual(response.data[0]['slug'], self.category.slug)

    def test_retrieve_category_detail(self):
        detail_url = reverse('categories:category-detail', kwargs={'pk': self.category.id})
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.category.name)
        self.assertEqual(response.data['description'], self.category.description)
        self.assertEqual(response.data['is_featured'], self.category.is_featured)
        self.assertEqual(response.data['tags'], self.category.tags)
        self.assertEqual(response.data['slug'], self.category.slug)

    def test_update_category(self):
        update_data = {
            'name': 'Updated Category',
            'description': 'This is an updated category.',
            'is_featured': False,
            'tags': 'tag3, tag4',
            'slug': 'updated-category',
        }
        response = self.client.put(reverse('categories:category-detail', kwargs={'pk': self.category.id}), update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_category = Category.objects.get(id=self.category.id)
        self.assertEqual(updated_category.name, 'Updated Category')
        self.assertEqual(updated_category.description, 'This is an updated category.')
        self.assertEqual(updated_category.is_featured, False)
        self.assertEqual(updated_category.tags, 'tag3, tag4')
        self.assertEqual(updated_category.slug, 'updated-category')

    def test_delete_category(self):
        response = self.client.delete(reverse('categories:category-detail', kwargs={'pk': self.category.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)
