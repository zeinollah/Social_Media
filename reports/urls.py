from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostReportView, AccountReportView

router = DefaultRouter()
router.register(r"post_report", PostReportView, basename="post_report")
router.register(r"account_report", AccountReportView, basename="account_report")


urlpatterns = [
    path('', include(router.urls)),
]


