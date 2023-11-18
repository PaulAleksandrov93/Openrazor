from django.urls import path
from .views import get_user_profiles, get_user_profile, create_user_profile, update_user_profile, delete_user_profile

app_name = 'profiles'

urlpatterns = [
    path('user_profiles/', get_user_profiles, name='get_user_profiles'),
    path('user_profiles/<int:pk>/', get_user_profile, name='get_user_profile'),
    path('create_user_profile/', create_user_profile, name='create_user_profile'),
    path('update_user_profile/<int:pk>/', update_user_profile, name='update_user_profile'),
    path('delete_user_profile/<int:pk>/', delete_user_profile, name='delete_user_profile'),
]