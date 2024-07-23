from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import CustomerInformation, AccountInformation, TransactionInformation, LoanInformation, CreditCardInformation
from .serializers import CustomerInformationSerializer, AccountInformationSerializer, TransactionInformationSerializer, LoanInformationSerializer, CreditCardInformationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from transformers import pipeline

class CustomerInformationViewSet(viewsets.ModelViewSet):
    queryset = CustomerInformation.objects.all()
    serializer_class = CustomerInformationSerializer

class AccountInformationViewSet(viewsets.ModelViewSet):
    queryset = AccountInformation.objects.all()
    serializer_class = AccountInformationSerializer

class TransactionInformationViewSet(viewsets.ModelViewSet):
    queryset = TransactionInformation.objects.all()
    serializer_class = TransactionInformationSerializer

class LoanInformationViewSet(viewsets.ModelViewSet):
    queryset = LoanInformation.objects.all()
    serializer_class = LoanInformationSerializer

class CreditCardInformationViewSet(viewsets.ModelViewSet):
    queryset = CreditCardInformation.objects.all()
    serializer_class = CreditCardInformationSerializer

@api_view(['POST'])
def chat(request):
    query = request.data.get('query')
    model_name = "distilbert-base-uncased-distilled-squad"
    nlp = pipeline("question-answering", model=model_name)
    context = "Your context from the database"
    result = nlp(question=query, context=context)
    return Response({"response": result['answer']})
