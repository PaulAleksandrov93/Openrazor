from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from .models import UserProfile

class UserProfileTests(APITestCase):
    def setUp(self):
        # Создаем тестового пользователя
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Создаем тестовый профиль пользователя
        self.profile_data = {
            'user': self.user.id,
            'bio': 'Test bio',
            'age': 25,
            'date_of_birth': '1998-01-01'
        }

    def test_create_user_profile(self):
        # Создаем профиль
        response = self.client.post('/api/profiles/', self.profile_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserProfile.objects.count(), 1)
        self.assertEqual(UserProfile.objects.get().bio, 'Test bio')

    def test_get_user_profiles(self):
        # Получаем список профилей
        response = self.client.get('/api/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), UserProfile.objects.count())

    def test_get_user_profile(self):
        # Получаем конкретный профиль
        profile = UserProfile.objects.create(user=self.user, bio='Test bio', age=25, date_of_birth='1998-01-01')
        response = self.client.get(f'/api/profiles/{profile.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['bio'], 'Test bio')

    def test_update_user_profile(self):
        # Обновляем профиль
        profile = UserProfile.objects.create(user=self.user, bio='Test bio', age=25, date_of_birth='1998-01-01')
        updated_data = {'bio': 'Updated bio', 'age': 30, 'date_of_birth': '1992-01-01'}
        response = self.client.put(f'/api/profiles/{profile.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(UserProfile.objects.get(id=profile.id).bio, 'Updated bio')

    def test_delete_user_profile(self):
        # Удаляем профиль
        profile = UserProfile.objects.create(user=self.user, bio='Test bio', age=25, date_of_birth='1998-01-01')
        response = self.client.delete(f'/api/profiles/{profile.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(UserProfile.objects.count(), 0)