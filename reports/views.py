from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from reports.models import PostReport, AccountReport
from reports.serializers import PostReportSerializer, AccountReportSerializer


class PostReportView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PostReport.objects.all()
    serializer_class = PostReportSerializer
    search_fields = ['id', 'title', 'reporter__username']
    http_method_names = ['post', 'get']


    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def get_queryset(self):
        if self.request.user.is_superuser:
            return PostReport.objects.all()
        else:
            return PostReport.objects.filter(reporter=self.request.user)


class AccountReportView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AccountReport.objects.all()
    serializer_class = AccountReportSerializer
    search_fields = ['id','account__username']
    http_method_names = ['post', 'get']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def get_queryset(self):
        if self.request.user.is_superuser:
            return AccountReport.objects.all()
        else:
            return AccountReport.objects.filter(reporter=self.request.user)