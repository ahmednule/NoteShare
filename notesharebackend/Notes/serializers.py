from rest_framework import serializers
from .models import File

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
    subject = serializers.CharField()

class FileUploadSeralizer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'filename', 'content', 'date_created', 'user', 'subject']
        read_only_fields = ['date_created']

class FileRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'filename', 'content', 'user']