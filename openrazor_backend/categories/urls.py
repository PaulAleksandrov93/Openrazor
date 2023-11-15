from django.urls import path
from . import views

app_name = 'categories'

urlpatterns = [
    path('categories/', views.getCategories, name='get_categories'),
    path('categories/<int:pk>/', views.getCategory, name='get_category'),
    path('categories/create/', views.createCategory, name='create_category'),
    path('categories/update/<int:pk>/', views.updateCategory, name='update_category'),
    path('categories/delete/<int:pk>/', views.deleteCategory, name='delete_category'),
]