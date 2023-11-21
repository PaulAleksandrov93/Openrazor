import json
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from .models import SocialNetwork

class SocialNetworkViewsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.social_network = SocialNetwork.objects.create(name='Test Network', link='https://example.com')

    def test_get_social_network_list(self):
        response = self.client.get('/api/social-networks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], 'Test Network')

    def test_create_social_network(self):
        data = {'name': 'New Network', 'link': 'https://newexample.com'}
        response = self.client.post('/api/social-networks/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SocialNetwork.objects.count(), 2)
        self.assertEqual(SocialNetwork.objects.last().name, 'New Network')

    def test_get_social_network_detail(self):
        response = self.client.get(f'/api/social-networks/{self.social_network.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data['name'], 'Test Network')

    def test_update_social_network(self):
        data = {'name': 'Updated Network', 'link': 'https://updatedexample.com'}
        response = self.client.put(f'/api/social-networks/{self.social_network.pk}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.social_network.refresh_from_db()
        self.assertEqual(self.social_network.name, 'Updated Network')

    def test_delete_social_network(self):
        response = self.client.delete(f'/api/social-networks/{self.social_network.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(SocialNetwork.objects.count(), 0)
