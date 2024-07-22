from rest_framework import serializers
from .models import CustomerInformation

class CustomerInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerInformation
        fields = '__all__'
