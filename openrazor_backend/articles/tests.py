from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Article
from rest_framework import status
import json

class ArticleTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.article = Article.objects.create(title='Test Article', content='Test Content', author=self.user, tags='test')

    def test_get_article_list(self):
        response = self.client.get('/articles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_article(self):
        self.client.force_login(self.user)
        data = {
            'title': 'New Article',
            'content': 'New Content',
            'tags': 'new'
        }
        response = self.client.post('/articles/create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_article_detail(self):
        response = self.client.get(f'/articles/{self.article.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_article(self):
        self.client.force_login(self.user)
        data = {
            'title': 'Updated Article',
            'content': 'Updated Content',
            'tags': 'updated'
        }
        response = self.client.put(f'/articles/update/{self.article.pk}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_article(self):
        self.client.force_login(self.user)
        response = self.client.delete(f'/articles/delete/{self.article.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)