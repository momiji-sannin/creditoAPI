from rest_framework import serializers
from creditscore.models import Client, Address, Application


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'gender', 'age', 'monthly_income', 'rfc']


class Application(serializers.ModelSerializer):
    class Meta:
        model =  Application
        fields = ['id', 'created_at', 'client']
    client = serializers.HyperlinkedRelatedField(
        queryset=Client.objects.all(),
        view_name='client-detail'
    )