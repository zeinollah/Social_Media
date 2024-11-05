from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from accounts import serializers
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
    search_fields = ['title','text',]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != self.request.user and not request.user.is_superuser:
            raise PermissionDenied("You do not have permission to delete this post.")
        self.perform_destroy(instance)
        return Response({'detail': 'Post deleted'}, status=status.HTTP_204_NO_CONTENT)

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

    def perform_create(self, serializer):
        post_id = self.request.data.get('post')
        if not post_id:
            raise ValidationError("You must provide a post_id.")

        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            raise Http404("Post does not exist.")

        serializer.save(author=self.request.user, post=post)