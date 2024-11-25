from django.urls import path
from .views import (
    RequestView,
    RequestListView,
    RequestStatusView
)

urlpatterns = [
    path('Request/', RequestView.as_view(), name='request'),
    path('Request_list/', RequestListView.as_view(), name='request_list'),
    path('Request_status/', RequestStatusView.as_view(), name='request_status'),
]