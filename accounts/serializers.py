from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from accounts.models import Profile

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
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
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
        search_fields = ['first_name', 'last_name', 'username',]
        read_only_fields = ['id', 'created_on']

    def create(self, validated_data):
        user = User(
            username=validated_data.get('username'),
            email=validated_data['email'],
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.password = validated_data.get('password', instance.password)

        instance.save()
        return instance

    def delete(self, instance):
        if not self.context['request'].user.is_authenticated:
            raise serializers.ValidationError("You do not have permission to delete this user.")
        instance.delete()
        return {'detail': 'User deleted successfully.'}




class ProfileSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(
        required=False,
        validators=[UniqueValidator(
            queryset=Profile.objects.all(),
            message="Phone number already used",
        )]
    )

    class Meta:
        model = Profile
        fields = ['user', 'phone_number', 'bio', 'birth_date', 'gender', 'last_login', 'created_on', 'updated_on']
        search_fields = ['user']
        read_only_fields = ['last_login', 'created_on', 'updated_on','ip_address']

    def create(self, validated_data):
        profile = Profile(
            user=validated_data.get('user'),
            phone_number=validated_data.get('phone_number'),
            bio=validated_data.get('bio'),
            birth_date=validated_data.get('birth_date'),
            gender=validated_data.get('gender'),
        )
        profile.save()
        return profile

    def update(self, instance, validated_data): #TODO : we got "detail": "No Profile matches the given query." for PATCH
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.image = validated_data.get('image', instance.image)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.gender = validated_data.get('gender', instance.gender)

        instance.save()
        return instance

