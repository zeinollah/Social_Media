from django.urls import path
from .views import UserListView,RequestView



urlpatterns = [
    path('User-list/', UserListView.as_view(), name='User_list'),
    path('Request/', RequestView.as_view(), name='request'),
]