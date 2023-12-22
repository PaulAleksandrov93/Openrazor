from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
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