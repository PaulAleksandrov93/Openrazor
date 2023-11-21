from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import StoreContact

class StoreContactTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.contact = StoreContact.objects.create(
            city='Test City',
            address='Test Address',
            phone='123-456-7890',
            email='test@example.com',
            working_hours='9 AM - 5 PM'
        )

    def test_store_contact_detail(self):
        url = reverse('store_contact_detail')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['city'], self.contact.city)

    def test_store_contact_list(self):
        url = reverse('store_contact_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_store_contact_create(self):
        url = reverse('store_contact_create')
        data = {
            'city': 'New City',
            'address': 'New Address',
            'phone': '987-654-3210',
            'email': 'new@example.com',
            'working_hours': '10 AM - 6 PM'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(StoreContact.objects.count(), 2)

    def test_store_contact_detail_api(self):
        url = reverse('store_contact_detail_api', args=[self.contact.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['city'], self.contact.city)

    def test_store_contact_update_api(self):
        url = reverse('store_contact_detail_api', args=[self.contact.id])
        data = {
            'city': 'Updated City',
            'address': 'Updated Address',
            'phone': '987-654-3210',
            'email': 'updated@example.com',
            'working_hours': '10 AM - 6 PM'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.contact.refresh_from_db()
        self.assertEqual(self.contact.city, 'Updated City')

    def test_store_contact_delete_api(self):
        url = reverse('store_contact_detail_api', args=[self.contact.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(StoreContact.objects.count(), 0)
