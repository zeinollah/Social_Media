from operator import imatmul
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from accounts.models import Profile ,Account

User = get_user_model()

class AccountSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(
            queryset=User.objects.all(),
            message="Email already used",
        )]
    )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(
            queryset=User.objects.all(),
            message="Username already exists",
            )]
    )
    first_name = serializers.CharField(required=True,)
    last_name = serializers.CharField(required=True,)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = '__all__'
        search_fields = ['first_name', 'last_name', 'username',]

    def create(self, validated_data):
        user = User(
            username=validated_data.get('username'),
            email=validated_data['email'],
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            password=validated_data.get('password'),
        )
        user.save()
        return user



# class ProfileSerializer(serializers.ModelSerializer):

