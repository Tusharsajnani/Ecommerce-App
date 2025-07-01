from django.shortcuts import render
from store.shipment.models import Shipment
from store.shipment.serializers import ShipmentSerializer  # Correct import
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

class Shipmentview(APIView):
    def get(self,request,format=None):
        store = Shipment.objects.all()
        serializer = ShipmentSerializer(store,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,format=None):
        serializer = ShipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)