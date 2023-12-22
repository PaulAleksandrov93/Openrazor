from django.urls import path
from .views import get_user_profiles, get_user_profile, create_user_profile, update_user_profile, delete_user_profile, getRoutes
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)

app_name = 'profiles'

urlpatterns = [
    path('', getRoutes),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('user_profiles/', get_user_profiles, name='get_user_profiles'),
    path('user_profiles/<int:pk>/', get_user_profile, name='get_user_profile'),
    path('create_user_profile/', create_user_profile, name='create_user_profile'),
    path('update_user_profile/<int:pk>/', update_user_profile, name='update_user_profile'),
    path('delete_user_profile/<int:pk>/', delete_user_profile, name='delete_user_profile'),
]