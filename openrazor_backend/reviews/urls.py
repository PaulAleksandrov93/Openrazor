from django.urls import path
from .views import get_product_reviews, create_review, update_review, delete_review

app_name = 'reviews'

urlpatterns = [
    path('product/<int:product_id>/', get_product_reviews, name='get_product_reviews'),
    path('product/<int:product_id>/create/', create_review, name='create_review'),
    path('review/<int:review_id>/update/', update_review, name='update_review'),
    path('review/<int:review_id>/delete/', delete_review, name='delete_review'),
]