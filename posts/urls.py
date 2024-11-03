from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, PostFileViewSet, CommentViewSet




router = DefaultRouter()
router.register(r"post", PostViewSet, basename="post")
router.register(r"post_file", PostFileViewSet, basename="post_file")
router.register(r"comments", CommentViewSet, basename="comments")

urlpatterns = [
    path('', include(router.urls)),

]