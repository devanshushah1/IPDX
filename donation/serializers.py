from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField, ModelSerializer
from .models import *

class NgoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ngos
        fields = ['user_id', 'name', 'phone']

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donors
        fields = ['user_id', 'name', 'phone']

class ReqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirements
        fields = '__all__'