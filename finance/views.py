from rest_framework import viewsets
from .models import FinancialRecord
from .serializers import FinancialRecordSerializer
from .permissions import RoleBasedPermission
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from rest_framework import status

class FinancialRecordViewSet(viewsets.ModelViewSet):
    queryset = FinancialRecord.objects.all()
    serializer_class = FinancialRecordSerializer
    permission_classes = [RoleBasedPermission]

    def get_queryset(self):
        user = self.request.user
        queryset = FinancialRecord.objects.all()

        # 🔐 Role-based access
        if user.role == 'viewer':
            queryset = queryset.filter(user=user)

        # 🔍 Filters
        type_param = self.request.query_params.get('type')
        category = self.request.query_params.get('category')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        if type_param:
            queryset = queryset.filter(type=type_param)

        if category:
            queryset = queryset.filter(category=category)

        if start_date and end_date:
            queryset = queryset.filter(date__range=[start_date, end_date])

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@api_view(['GET'])
def dashboard_summary(request):
    user = request.user

    # Role-based data selection
    if user.role == 'viewer':
        records = FinancialRecord.objects.filter(user=user)
    else:
        records = FinancialRecord.objects.all()

    # totals
    total_income = records.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = records.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0

    balance = total_income - total_expense

    #category-wise expense
    category_data = (
        records.filter(type='expense')
        .values('category')
        .annotate(total=Sum('amount'))
    )

    return Response({
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance,
        "category_expense": category_data
    })