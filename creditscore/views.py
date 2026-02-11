from rest_framework import status
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Address, Client, Application
from .serializer import ClientSerializer, AddressSerializer, ApplicationSerializer

# Create your views here.
class ApplicationViewSet(CreateModelMixin, 
                  RetrieveModelMixin, 
                  DestroyModelMixin, 
                  GenericViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer