from rest_framework import serializers
from .models import File

class FileSerializer(serializers.Serializer):
    file = serializers.FileField()
    subject = serializers.CharField(max_length=100)
    user = serializers.CurrentUserDefault()

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'filename', 'content', 'date_created', 'user', 'subject']
        read_only_fields = ['date_created']

class FileRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'filename', 'content', 'user']