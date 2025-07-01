from django.shortcuts import render
from store.payment.models import Payment

from rest_framework.views import APIView
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from store.payment.serializers import Paymentserializer



class Paymentview(APIView):
    def get(self,request,format=None):
        store = Payment.objects.all()
        serializer = Paymentserializer(store,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,format=None):
        serializer = Paymentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)