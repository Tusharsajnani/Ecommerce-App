# from django.shortcuts import render
from store.user.serializers import *
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


class Userview(APIView):
    def get(self,request,format=None):
        store = User.objects.all()
        serializer = Userserializer(store,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        print(f"\n\n\n DATA {request.data} \n\n\n")
        serializer = Userserializer(data=request.data)
        if serializer.is_valid():
            # print("VALID SERIALIZER \n\n")
            serializer.save()
            # print("WORKING OR NOT \n\n")
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class Usercrud(APIView):
    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        
    def get(self,request,pk,format=None):
        curd = self.get_object(pk)
        serializer = Userserializer(curd)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED) 








# #from rest_framework import viewsets
# from .models import User
# from .serializers import UserSerializers
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# @api_view(['GET'])
# def get_all_user(request):
#     users = User.objects.all()
#     serializer = UserSerializers(users, many=True)
#     return Response(serializer.data)


# @api_view(['POST'])
# def create_user(request):
#     serializers= UserSerializers(data=request.data)
#     if serializers.is_valid():
#         serializers.save()
#         return Response(serializers.data, status=status.HTTP_201_CREATED)
#     return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def get_all_users_by_ID(request, pk):
#     try:
#         user_instance = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

#     serializer = UserSerializers(user_instance)
#     return Response(serializer.data)

# @api_view(['PUT'])
# def update_user(request, pk):
#     try:
#         user_instance = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

#     serializer = UserSerializers(user_instance, data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['DELETE'])
# def delete_user(request, pk):
#     try:
#         user_instance = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

#     user_instance.delete()
#     return Response({'message': 'Student deleted'}, status=status.HTTP_204_NO_CONTENT)
