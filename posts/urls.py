from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (PostViewSet,
                    PostFileViewSet,
                    CommentViewSet,
                    LikeViewSet,
)

router = DefaultRouter()
router.register(r"post", PostViewSet, basename="posts")
router.register(r"post_file", PostFileViewSet, basename="post_files")
router.register(r"comments", CommentViewSet, basename="comments")
router.register(r"like", LikeViewSet, basename="likes")

urlpatterns = [
    path('', include(router.urls)),
]