from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import generics
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.apis.serializers import UserSerializer, GroupSerializer, RegionSerializer, CitySerializer, TownSerializer, MedalSerializer
from apps.pokemon.models import Region, City, Town, Medal
from django.http import Http404

# Create your views here.


# class RegionView(APIView):
#     """
# 	Se listan todas las Regiones existentes ó
# 	Se crea una nueva Region
# 	"""
#
#     def get(self, request, format=None):
#         regiones = Region.objects.all()
#         serializer = RegionSerializer(regiones, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = RegionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegionView(generics.ListCreateAPIView):
    """Listado de todas las regioness Existentes."""
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class CityView(generics.ListCreateAPIView):
    """Listado de todas las regiones Existentes
    con opción de crear nuevas.
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer


class TownView(generics.ListCreateAPIView):
    """Listado de todos los pueblos Existentes
    con opción de crear nuevos.
    """
    queryset = Town.objects.all()
    serializer_class = TownSerializer


class MedalView(generics.ListCreateAPIView):
    queryset = Medal.objects.all()
    serializer_class = MedalSerializer