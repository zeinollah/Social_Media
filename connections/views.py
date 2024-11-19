from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserListSerializer, FriendshipSerializer
from .models import Connection





User = get_user_model()

class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.filter(is_superuser=False, is_staff=False,)
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)


class RequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        username = request.data.get('username')

        try:
            receiver = User.objects.get(username=username)
            sender_profile = request.user.profiles
            recipient_profile = receiver.profiles

            Connection.objects.create(
                request_sender=sender_profile,
                request_receiver=recipient_profile
            )
            return Response({"detail": "Request sent"},status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({"detail": "User not found"},status=status.HTTP_404_NOT_FOUND)


    def get(self, request):
        requests = Connection.objects.all()
        serializer = FriendshipSerializer(requests, many=True)
        return Response({"requests": serializer.data}, status=status.HTTP_200_OK)





