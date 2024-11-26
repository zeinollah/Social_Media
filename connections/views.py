from http.client import responses
from django.contrib.auth import get_user_model
from django.db import connection
from django.db.models import Q
from django.utils.html import strip_tags
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import Profile
from .serializers import RequestListSerializer, ConnectionSerializer
from .models import Connection





User = get_user_model()
class RequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        username = request.data.get('username')
        try:
            receiver = User.objects.get(username=username)
            sender_profile = request.user.profiles
            recipient_profile = receiver.profiles

            Connection.objects.get_or_create(
                request_sender=sender_profile,
                request_receiver=recipient_profile
            )
            return Response({"detail": "Request sent"},status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({"detail": "User not found"},status=status.HTTP_404_NOT_FOUND)


    def get(self, request):
        requests = Connection.objects.all()
        serializer = ConnectionSerializer(requests, many=True)
        if not request.user.is_superuser:
            return Response({"detail": "Only admin allow to check "},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            return Response({"requests": serializer.data}, status=status.HTTP_200_OK)


class RequestListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        connections = Connection.objects.filter(request_receiver=request.user.profiles, status='Pending')
        users = [co.request_sender.user for co in connections]
        serializer = RequestListSerializer(users, many=True)
        return Response(serializer.data)


class RequestStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        username = request.data.get('username')
        request_status = request.data.get('status')

        if not username:
            return Response({"detail": "Username is required"},status=status.HTTP_400_BAD_REQUEST)

        if not request_status:
            return Response({"detail": "Status is required"},status=status.HTTP_400_BAD_REQUEST)

        if request_status not in ['Accepted', 'Rejected']:
            return Response({"detail": "Only [Accepted] and [Rejected] are allow to choose"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            sender_profile = Profile.objects.get(user__username=username)
            receiver_profile = Profile.objects.get(user=request.user)
            connections = Connection.objects.get(request_sender=sender_profile, request_receiver=receiver_profile, status='Pending')

        except Profile.DoesNotExist:
            return Response({"detail": "User not found"},status=status.HTTP_404_NOT_FOUND)

        except Connection.DoesNotExist:
            return Response({"detail": "Request not found"},status=status.HTTP_404_NOT_FOUND)

        if request_status == 'Accepted':
            connections.status = Connection.ACCEPTED
            responses_message = "Request Accepted"
        else:
            connections.status = Connection.REJECTED
            responses_message = "Request Rejected"

        connections.save()
        return Response({"detail": responses_message},status=status.HTTP_200_OK)


class FriendShipListView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request):
        connections = Connection.objects.filter(
            Q(request_receiver=request.user.profiles) |
            Q(request_sender=request.user.profiles),
            status='Accepted'
        )
        users = [co.request_sender.user for co in connections]
        serializer = RequestListSerializer(users, many=True)
        return Response(serializer.data)


