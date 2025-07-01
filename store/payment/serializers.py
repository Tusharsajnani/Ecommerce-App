from store.models import Payment
from rest_framework import serializers

class Paymentserializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields =  ['payment_id','payment_method','amount','user_id']