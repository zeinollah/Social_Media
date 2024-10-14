from django.contrib.auth import get_user_model
from rest_framework import viewsets
from accounts.serializers import AccountSerializer



User = get_user_model()
class AccountAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

