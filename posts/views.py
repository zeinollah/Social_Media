from rest_framework import viewsets, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from posts.models import Post, PostFile
from posts.serializers import PostSerializer, PostFileSerializer




class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter]
    search_fields = [
        'title',
        'text',
    ]

    def perform_create(self, serializer):
        post = serializer.save()
        post.author.profiles.save()

    def perform_update(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if not request.user.is_authenticated:
            raise PermissionDenied("You do not have permission to delete this post.")
        self.perform_destroy(instance)
        return Response({'detail': 'Post deleted'}, status=status.HTTP_204_NO_CONTENT)


class PostListViewSer(viewsets.ReadOnlyModelViewSet):
    pass
#TODO: write to user can take post list filter by public.


class PostFileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PostFile.objects.all()
    serializer_class = PostFileSerializer
    filter_backends = [SearchFilter]
    search_fields = ['post']

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if not request.user.is_authenticated:
            raise PermissionDenied("You do not have permission to delete this file.")
        self.perform_destroy(instance)
        return Response({'detail': 'File deleted'}, status=status.HTTP_204_NO_CONTENT)