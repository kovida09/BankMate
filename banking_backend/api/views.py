from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import CustomerInformation
from .serializers import CustomerInformationSerializer

class CustomerInformationViewSet(viewsets.ModelViewSet):
    queryset = CustomerInformation.objects.all()
    serializer_class = CustomerInformationSerializer
