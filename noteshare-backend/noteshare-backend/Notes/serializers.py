# api/serializers.py

from rest_framework import serializers
from .models import Notes

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'
