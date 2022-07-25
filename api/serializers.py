# python object to json format
from rest_framework import serializers
from .models import Plant, UserPlant

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'

class UserPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlant
        fields = '__all__'