from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.models import Profile
from accounts.serializers import UserSerializer, ProfileSerializer



User = get_user_model()
class UserAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    search_fields = ['first_name', 'last_name', 'username', ]


class ProfileAPIView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['user']

    #TODO: write save ip_address def .



