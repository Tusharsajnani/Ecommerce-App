from rest_framework import serializers
from store.orders.models import Order

class Orderserializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields =  '__all__'