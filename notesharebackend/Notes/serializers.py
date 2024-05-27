from rest_framework import serializers
from .models import Resource, UserUpload

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'title', 'description', 'file', 'uploaded_by', 'created_at']

class UserUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserUpload
        fields = ['id', 'user', 'file', 'uploaded_at']
