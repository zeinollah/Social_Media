from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountAPIView


router = DefaultRouter()
router.register(r"sign up",AccountAPIView, basename="sign up")

urlpatterns = [
    path('', include(router.urls)),

]