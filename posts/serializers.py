from rest_framework import serializers, status
from posts.models import Post, PostFile, Comment, Like


class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='author.username', read_only=True)
    post_id = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = Post
        fields = ['post_id', 'username', 'title', 'text', 'is_public', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def validate(self, attrs):

        if len(attrs.get('text')) > 1000:
            raise serializers.ValidationError("Text could not longer than 1000 characters")

        return attrs



class PostFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostFile
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

    def validate(self, attrs):

        if len(attrs.get('caption')) > 500:
            raise serializers.ValidationError("Caption could not longer than 500 characters")

        return attrs
#TODO: fix the PATCH method



class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    comment_id = serializers.IntegerField(source='id', read_only=True)
    post_id = serializers.IntegerField(source='post.id', read_only=True)

    class Meta:
        model = Comment
        fields = ['author_username', 'comment_id', 'post_id', 'comment', 'created_on']
        read_only_fields = ['created_on', 'author_username', 'comment_id','post_id']

    def validate(self, attrs):
        if len(attrs.get('comment')) > 150:
            raise serializers.ValidationError("Comment could not longer than 150 characters")

        return attrs



class LikeSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Like
        fields = ['author_username', 'post','is_liked', 'dislike', 'created_at', 'updated_at']
        read_only_fields = ['author_username', 'created_at', 'updated_at']


    def validate(self, attrs):
        post = attrs.get('post')
        if not Post.objects.filter(id=post.id).exists():
            raise serializers.ValidationError({"post": ["Post does not exist."]}, status.HTTP_404_NOT_FOUND)

        return attrs
