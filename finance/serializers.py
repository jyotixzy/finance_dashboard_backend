from rest_framework import serializers
from .models import FinancialRecord

class FinancialRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialRecord
        fields = '__all__'

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than 0")
        return value

    def validate_type(self, value):
        if value not in ['income', 'expense']:
            raise serializers.ValidationError("Invalid type")
        return value

    def validate(self, data):
        type = data.get('type')
        category = data.get('category')
        amount = data.get('amount')

        income_categories = ['salary', 'business', 'investment']
        expense_categories = ['food', 'rent', 'travel', 'shopping']

        # 🔹 category validation
        if type == 'income' and category not in income_categories:
            raise serializers.ValidationError("Invalid category for income")

        if type == 'expense' and category not in expense_categories:
            raise serializers.ValidationError("Invalid category for expense")

        # 🔹 extra business rule
        if type == 'expense' and amount > 1000000:
            raise serializers.ValidationError("Expense too large")

        return data