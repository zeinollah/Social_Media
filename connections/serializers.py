from django.contrib.auth import get_user_model
from rest_framework import serializers
from connections.models import Connection

User = get_user_model()

class RequestListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["username", "image"]
        read_only_fields = ["username"]

    def get_image(self, instance):
        if hasattr(instance, 'image') and instance.profile.image:
            return instance.profile.image.url
        return ""




class ConnectionSerializer(serializers.ModelSerializer):
    request_id = serializers.PrimaryKeyRelatedField(source='id', read_only=True)
    request_sender = serializers.CharField(source='request_sender.user', read_only=True)
    request_receiver = serializers.CharField(source='request_receiver.user', read_only=True)

    class Meta:
        model = Connection
        fields = ('request_id', 'request_sender', 'request_receiver', 'status', 'created_at', 'updated_at')
        read_only_fields = ['status', 'created_at', 'updated_at']