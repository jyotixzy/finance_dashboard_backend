from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import FinancialRecordViewSet, dashboard_summary

router = DefaultRouter()
router.register(r'records', FinancialRecordViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('summary/', dashboard_summary),
]