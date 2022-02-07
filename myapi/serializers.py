from rest_framework import serializers
from .models import Installation, Status


class InstallationSerializer(serializers.Serializer):
    """Serializer to map the Model instance into JSON format."""

    id = serializers.IntegerField(read_only=True)
    customer_name = serializers.CharField(max_length=200)
    address = serializers.CharField()
    appointment_date = serializers.DateField()
    date_created = serializers.DateTimeField(required=False)
    date_modified = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        return Installation.objects.create(**validated_data)


class StatusSerializer(serializers.Serializer):
    """Serializer to map the Model instance into JSON format."""

    id = serializers.IntegerField(read_only=True)
    status = serializers.CharField(max_length=200)
    notes = serializers.CharField()
    date = serializers.DateTimeField(required=False)    
    installation_id = serializers.IntegerField()    

    def create(self, validated_data):
        return Status.objects.create(**validated_data)