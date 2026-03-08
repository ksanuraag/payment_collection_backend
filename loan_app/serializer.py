from rest_framework import serializers 
from .models import Payment,Customer


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model=Customer
        fields='__all__'

    def validate_account_no(self, value):
        if len(value) < 5:
            raise serializers.ValidationError(
                "Account number must be at least 5 characters"
            )
        return value

    def validate_interest_rate(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Interest rate must be greater than 0"
            )
        return value

    def validate_tenure(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Tenure must be greater than 0 months"
            )
        return value

    def validate_emi_due(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "EMI due must be greater than 0"
            )
        return value

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields='__all__'

    def validate_payment_amount(self,value):
        if value<=0:
            raise serializers.ValidationError("payment must be greater than 0")
        return value