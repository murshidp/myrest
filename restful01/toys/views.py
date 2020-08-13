from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ToySerializer
from rest_framework import status
from .models import Toy
# Create your views here.

@api_view(['GET','POST'])
def toy_list(request):
    if request.method=='GET':
        toys=Toy.objects.all()
        serializer=ToySerializer(toys,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=ToySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def toy_detail(request,pk):
    try:
        toy = Toy.objects.get(pk=pk)
    except toy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer=ToySerializer(toy)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer=ToySerializer(toy,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        toy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


