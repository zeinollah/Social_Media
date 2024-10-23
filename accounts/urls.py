from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserAPIView, ProfileAPIView

router = DefaultRouter()
router.register(r"sign_up",UserAPIView, basename="sign_up")
router.register(r"profile",ProfileAPIView, basename="profile")

urlpatterns = [
    path('', include(router.urls)),
]