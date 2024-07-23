from rest_framework import serializers
from .models import CustomerInformation ,AccountInformation, TransactionInformation, LoanInformation, CreditCardInformation

class CustomerInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerInformation
        fields = '__all__'

class AccountInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountInformation
        fields = '__all__'

class TransactionInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionInformation
        fields = '__all__'

class LoanInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanInformation
        fields = '__all__'

class CreditCardInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCardInformation
        fields = '__all__'