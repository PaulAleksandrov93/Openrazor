from django.urls import path
from .views import (
    store_contact_detail,
    store_contact_list,
    store_contact_create,
    store_contact_detail_api,
)

app_name = 'contacts'

urlpatterns = [
    path('contact/', store_contact_detail, name='store_contact_detail'),
    path('contacts/', store_contact_list, name='store_contact_list'),
    path('contacts/create/', store_contact_create, name='store_contact_create'),
    path('contacts/<int:pk>/', store_contact_detail_api, name='store_contact_detail_api'),
]