from django.shortcuts import render
from rest_framework import serializers, views, status
from rest_framework.parsers import MultiPartParser
from google.cloud import storage
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from google.auth import default

credentials, project_id = default()

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

class FileUploadView(views.APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = FileUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Get the uploaded file
        file = serializer.validated_data['file']

        # Create a Cloud Storage client
        client = storage.Client()

        # Get the bucket
        bucket = client.bucket('nyams-noteshare')

        # Create a new blob and upload the file
        blob = bucket.blob(file.name)
        blob.upload_from_file(file)

        # Return a success response
        return Response({'message': 'File uploaded successfully.'}, status=status.HTTP_201_CREATED)

