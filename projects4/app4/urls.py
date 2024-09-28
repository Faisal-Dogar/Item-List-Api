from django.urls import path
from .views import api_get_items, item_create_view, item_list_view

urlpatterns = [
    path('api/items/', api_get_items, name='api_get_items'),  # API endpoint
    path('', item_create_view, name='item_create'),  # Form to create new items
    path('items/', item_list_view, name='item_list'),  # List of items rendered from API data
]
