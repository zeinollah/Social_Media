from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from chats.models import Chat
from chats.serializers import ChatSerializer



class ChatView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


    def get_queryset(self):
        if self.request.user.is_superuser:
            return Chat.objects.all()
        else :
            return (
                Chat.objects.filter(sender= self.request.user) |
                Chat.objects.filter(receiver= self.request.user)
            )