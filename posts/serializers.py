from rest_framework import serializers
from posts.models import Post, PostFile, Comment


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



class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    comment_id = serializers.CharField(source='id', read_only=True)
    post_id = serializers.CharField(source='post.id', read_only=True)

    class Meta:
        model = Comment
        fields = ['author_username', 'comment_id', 'post_id', 'comment', 'created_on']
        read_only_fields = ['created_on']

    def validate(self, attrs):
        if len(attrs.get('comment')) > 150:
            raise serializers.ValidationError("Comment could not longer than 150 characters")

        if not Post.objects.exists():
            raise serializers.ValidationError("Post does not exist")

        return attrs