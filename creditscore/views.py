from rest_framework import status
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Address, Client, Application, Document
from .serializer import AddressSerializer, ApplicationSerializer, DocumentSerializer

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
