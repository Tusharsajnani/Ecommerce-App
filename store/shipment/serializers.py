from rest_framework import serializers
from store.models import Shipment  # Ensure Shipment is imported directly


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'
