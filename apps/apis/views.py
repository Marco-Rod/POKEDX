from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.apis.serializers import UserSerializer, GroupSerializer, RegionSerializer
from apps.pokemon.models import Region
from django.http import Http404

# Create your views here.


class RegionView(APIView):
    """
	Se listan todas las Regiones existentes ó
	Se crea una nueva Region
	"""

    def get(self, request, format=None):
        regiones = Region.objects.all()
        serializer = RegionSerializer(regiones, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RegionSerializer(data=request.data)
        if serializer.is_valid():
            print("Llegue sano y salvo :D")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
