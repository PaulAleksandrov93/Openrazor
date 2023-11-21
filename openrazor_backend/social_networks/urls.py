from django.urls import path
from .views import social_network_list, social_network_detail

app_name = 'social_networks'

urlpatterns = [
    path('social-networks/', social_network_list, name='social_network_list'),
    path('social-networks/<int:pk>/', social_network_detail, name='social_network_detail'),
]