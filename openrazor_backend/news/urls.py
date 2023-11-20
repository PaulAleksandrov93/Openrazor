from django.urls import path
from .views import get_news, get_news_detail, create_news, update_news, delete_news

app_name = 'news'

urlpatterns = [
    path('news/', get_news, name='get_news'),
    path('news/<int:pk>/', get_news_detail, name='get_news_detail'),
    path('news/create/', create_news, name='create_news'),
    path('news/update/<int:pk>/', update_news, name='update_news'),
    path('news/delete/<int:pk>/', delete_news, name='delete_news'),
]