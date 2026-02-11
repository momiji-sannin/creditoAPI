from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Address, Client, Application, Document
from .serializer import AddressSerializer, ApplicationSerializer, DocumentSerializer, GetStatusApplicationSerializer
from django.shortcuts import render
import random

# Create your views here.
class ApplicationViewSet(CreateModelMixin, 
                  RetrieveModelMixin, 
                  DestroyModelMixin, 
                  GenericViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class DocumentViewSet(ModelViewSet):
    serializer_class = DocumentSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        appItem = Application.objects.filter(pk=self.kwargs['application_pk']).values('client_id')[0]
        return Document.objects.filter(client_id=appItem['client_id'])

    def get_serializer_context(self):
        appItem = Application.objects.filter(pk=self.kwargs['application_pk']).values('client_id')[0]
        return {'client_id' : appItem['client_id']}


@api_view(['GET'])
def calculate_score(request, app_pk):
    application = get_object_or_404(Application, pk=app_pk)
    result = random.randint(300, 900)   
    application.score = result
    if request.method == "GET":
        serializer = GetStatusApplicationSerializer(application, data= {"score" : result})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    return render(request, "creditscore/score.html", {"result" : result})
