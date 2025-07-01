#from rest_framework import viewsets
from .models import Product
from rest_framework import  status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Productserializer

@api_view(['GET'])
def get_all_products(request):
    products = Product.objects.all()
    serializer = Productserializer(products,many=True)
    return Response (serializer.data)

@api_view(['POST'])
def add_product(request):
    serializers= Productserializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

