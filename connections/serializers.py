from django.contrib.auth import get_user_model
from rest_framework import serializers
from connections.models import Friendship



User = get_user_model()

class UserListSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='id', queryset=User.objects.all())

    class Meta:
        model = User
        fields = ["user_id","username", "email"]
        read_only_fields = ["username", "email"]



class FriendshipSerializer(serializers.ModelSerializer):
    request_id = serializers.PrimaryKeyRelatedField(source='id', queryset=Friendship.objects.all())
    request_sender = serializers.CharField(source='request_sender.user.username')
    request_receiver = serializers.CharField(source='request_receiver.user.username')

    class Meta:
        model = Friendship
        fields = ('request_id', 'request_sender', 'request_receiver', 'status', 'created_at', 'updated_at')
        read_only_fields = ['status', 'created_at', 'updated_at']