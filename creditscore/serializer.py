from rest_framework import serializers
from creditscore.models import Client, Address, Application, Document


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'gender', 'age', 'monthly_income', 'rfc']


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Application
        fields = ['id', 'client', 'score', 'created_at',]
    id = serializers.UUIDField(read_only = True)
    score = serializers.IntegerField(read_only=True)
    client = ClientSerializer()

    def create(self, validated_data):
        client_data = validated_data.pop('client')
        client_rfc = client_data.pop('rfc')
        client_model, _ = Client.objects.update_or_create(rfc=client_rfc, defaults=client_data)

        appItem = Application.objects.create(client=client_model, **validated_data)

        return appItem


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Address
        fields = ['id', 'street', 'city', 'zip', 'client']
    client = serializers.HyperlinkedRelatedField(
        queryset=Client.objects.all(),
        view_name='client-detail'
    )

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['image', 'name']

    def create(self, validated_data):
        client_id = self.context['client_id']
        return Document.objects.create(client_id=client_id, **validated_data)

class GetStatusApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['status', 'score']
    status = serializers.SerializerMethodField(method_name='get_status')

    def get_status(self, item: Application) -> str:
        return  "Approved" if item.score > 500 else "Denied"