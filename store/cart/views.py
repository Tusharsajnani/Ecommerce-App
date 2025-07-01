from rest_framework import viewsets
from django.shortcuts import render
from store.cart import *
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cart
from .serializers import serializers,Cartserializer

class Cartview(APIView):
    def get(self,request,format=None):
        store = Cart.objects.all()
        serializer = Cartserializer(store,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,format=None):
        serializer = Cartserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class Cartcrud(APIView):
    def get_object(self,pk):
        try:
            return Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            raise Http404
        
    def get(self,request,pk,format=None):
        curd = self.get_object(pk)
        serializer = Cartserializer(curd)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk,format=None):
        curd = self.get_object(pk)
        serializer = Cartserializer(curd,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        curd = self.get_object(pk)
        curd.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)