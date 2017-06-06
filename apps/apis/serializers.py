from django.contrib.auth.models import User, Group
from rest_framework import serializers
from apps.pokemon.models import Region, City, Town, Medal


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Region
        fields = ('name', 'description')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
        # fields = ('name', 'description')


class TownSerializer(serializers.ModelSerializer):
    class Meta:
        model= Town
        fields = '__all__'


class MedalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medal
        fields = '__all__'