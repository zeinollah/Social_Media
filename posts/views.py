from rest_framework import viewsets, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from posts.models import (Post,
                          PostFile,
                          Comment,
                          )
from posts.serializers import (PostSerializer,
                               PostFileSerializer,
                               CommentSerializer,
                               )





class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter]
    search_fields = [
        'title',
        'text',
    ]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != self.request.user and not request.user.is_superuser:
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


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != self.request.user and not request.user.is_superuser:
            raise PermissionDenied("You do not have permission to delete this file.")
        self.perform_destroy(instance)
        return Response({'detail': 'File deleted'}, status=status.HTTP_204_NO_CONTENT)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
