from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostAPIView,PostFileAPIView

router = DefaultRouter()
router.register(r"post", PostAPIView, basename="post")
router.register(r"post_file", PostFileAPIView, basename="post_file")

urlpatterns = [
    path('', include(router.urls)),

]