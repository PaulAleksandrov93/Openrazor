from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('api/', include('products.urls', namespace='products')),
    path('api/', include('categories.urls', namespace='categories')),
    path('api/', include('profiles.urls', namespace='profiles')),
    path('api/', include('cart.urls', namespace='cart')),
    path('api/', include('orders.urls', namespace='orders')),
    path('api/', include('reviews.urls', namespace='reviews')),
    path('api/', include('articles.urls', namespace='articles')),
    path('api/', include('news.urls', namespace='news')),
    path('api/', include('contacts.urls', namespace='contacts')),
    path('api/', include('social_networks.urls', namespace='social_networks')),
]