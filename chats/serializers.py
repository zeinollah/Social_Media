from rest_framework import serializers
from accounts.serializers import User
from chats.models import Chat




class ChatSerializer(serializers.ModelSerializer):
    sender  = serializers.SlugRelatedField(
        slug_field='username',
        required=False,
        queryset=User.objects.all(),
    )
    receiver = serializers.SlugRelatedField(
        slug_field='username',
        required=False,
        queryset=User.objects.all(),
    )

    class Meta:
        model = Chat
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


    def validate(self, attrs):

        receiver = attrs.get('receiver')
        if not receiver:
            raise serializers.ValidationError({'receiver' : 'receiver is required'})


        context = attrs.get('context')
        if context and len(context) > 500:
            raise serializers.ValidationError({'context': 'context has limit for letter - only 500 '})

        return attrs


    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['sender'] = user

        receiver_user = validated_data.pop('receiver')
        validated_data['receiver'] = receiver_user
        return Chat.objects.create(**validated_data)