from rest_framework import serializers
from posts.models import Post, PostFile, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

    def validate(self, attrs):

        if len(attrs.get('text')) > 1000:
            raise serializers.ValidationError("text could not longer than 1000 characters")

        return attrs


    '''move def CRUD to views'''
    # def create(self, validated_data):
    #     post = Post.objects.create(**validated_data)
    #     post.auther.profile.save()
    #     return post
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.text = validated_data.get('text', instance.text)
    #     instance.is_public = validated_data.get('is_public', instance.is_public)
    #     instance.save()
    #     return instance
    #
    # def delete(self, instance):
    #     if not self.context['request'].user.is_authenticated:
    #         raise serializers.ValidationError("You do not have permission to delete this post.")
    #     instance.delete()
    #     return {'detail': 'Post deleted '}



class PostFileSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    video = serializers.FileField(required=False)
    file = serializers.FileField(required=False)

    class Meta:
        model = PostFile
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

    def validate(self, attrs):

        if len(attrs.get('caption')) > 500:
            raise serializers.ValidationError("caption could not longer than 500 characters")

        return attrs


    '''move def CRUD to views'''
    # def create(self, validated_data):
    #     postfile = PostFile.objects.create(**validated_data)
    #     return postfile
    #
    # def update(self, instance, validated_data):
    #     instance.image = validated_data.get('image', instance.image)
    #     instance.video = validated_data.get('video', instance.video)
    #     instance.file = validated_data.get('file', instance.file)
    #     instance.caption = validated_data.get('caption', instance.caption)
    #     instance.save()
    #     return instance
    #
    # def delete(self, instance):
    #     if not self.context['request'].user.is_authenticated:
    #         raise serializers.ValidationError("You do not have permission to delete this file.")
    #     instance.delete()
    #     return {'detail': 'File deleted '}



class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only = ['post','User']
