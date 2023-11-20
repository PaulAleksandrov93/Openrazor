from django.test import TestCase
from django.contrib.auth.models import User
from .models import News

class NewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.news_data = {
            'title': 'Test News',
            'content': 'This is a test news article.',
            'tags': 'test, news',
        }

    def test_create_news(self):
        self.client.force_login(self.user)
        response = self.client.post('/news/create/', self.news_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(News.objects.count(), 1)

    def test_get_news_list(self):
        response = self.client.get('/news/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 0)

        News.objects.create(title='News 1', content='Content 1', tags='tag1,tag2')
        News.objects.create(title='News 2', content='Content 2', tags='tag2,tag3')

        response = self.client.get('/news/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_get_news_detail(self):
        news = News.objects.create(**self.news_data)
        response = self.client.get(f'/news/{news.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['title'], 'Test News')

    def test_update_news(self):
        news = News.objects.create(**self.news_data)
        updated_data = {
            'title': 'Updated News',
            'content': 'Updated content',
            'tags': 'newtag1,newtag2',
        }

        self.client.force_login(self.user)
        response = self.client.put(f'/news/update/{news.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, 200)

        news.refresh_from_db()
        self.assertEqual(news.title, 'Updated News')
        self.assertEqual(news.tags, 'newtag1,newtag2')

    def test_delete_news(self):
        news = News.objects.create(**self.news_data)
        self.client.force_login(self.user)
        response = self.client.delete(f'/news/delete/{news.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(News.objects.count(), 0)