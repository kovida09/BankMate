from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import CustomerInformation, AccountInformation, TransactionInformation, LoanInformation, CreditCardInformation
from .serializers import CustomerInformationSerializer, AccountInformationSerializer, TransactionInformationSerializer, LoanInformationSerializer, CreditCardInformationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from transformers import pipeline
from django.http import JsonResponse

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
    customer_context = ""
    for customer in CustomerInformation.objects.all()[:5]:  # Limit the number of records for simplicity
        customer_context += f"Customer {customer.customer_id} named {customer.name} lives in {customer.city}, {customer.state}. "

    account_context = ""
    for account in AccountInformation.objects.all()[:5]:
        account_context += f"Account {account.account_id} of type {account.account_type} has balance {account.balance}. "
    
    context = customer_context + account_context
    result = nlp(question=query, context=context)
    return Response({"response": result['answer']})
