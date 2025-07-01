from store.models import *
from rest_framework import serializers

class Cartserializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['quantity', 'user_id', 'product_id']