from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import CustomerInformation
from .serializers import CustomerInformationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from transformers import pipeline

class CustomerInformationViewSet(viewsets.ModelViewSet):
    queryset = CustomerInformation.objects.all()
    serializer_class = CustomerInformationSerializer

@api_view(['POST'])
def chat(request):
    query = request.data.get('query')
    model_name = "distilbert-base-uncased-distilled-squad"
    nlp = pipeline("question-answering", model=model_name)
    context = "Your context from the database"
    result = nlp(question=query, context=context)
    return Response({"response": result['answer']})
