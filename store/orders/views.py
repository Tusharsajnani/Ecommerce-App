from django.shortcuts import render
from store.models import Order
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from store.orders.serializers import Orderserializer


class Orderview(APIView):
    def get(self,request,format=None):
        store = Order.objects.all()
        serializer = Orderserializer(store,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
       
    def post(self,request,format=True):
        serializer = Orderserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    