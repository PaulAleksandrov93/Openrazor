from django.urls import path
from .views import get_article_list, create_article, get_article_detail, update_article, delete_article

app_name = 'articles'

urlpatterns = [
    path('articles/', get_article_list, name='get_article_list'),
    path('articles/create/', create_article, name='create_article'),
    path('articles/<int:pk>/', get_article_detail, name='get_article_detail'),
    path('articles/update/<int:pk>/', update_article, name='update_article'),
    path('articles/delete/<int:pk>/', delete_article, name='delete_article'),
]