from django.shortcuts import render
from rest_framework import serializers, views, status
from rest_framework.parsers import MultiPartParser
from django.http import FileResponse
from google.cloud import storage
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from google.auth import default
from .serializers import FileSerializer
import os

credentials, project_id = default()
bucket_name ='nyams-noteshare'


class FileUploadView(views.APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        # Validate the file
        serializer = FileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Get the uploaded file
        file = serializer.validated_data['file']

        # Generate a unique filename with extension
        import uuid
        filename, extension = os.path.splitext(file.name)
        unique_filename = f'{filename}_{uuid.uuid4()}.{extension}'
        
        # Create a Cloud Storage client
        client = storage.Client()

        # Get the bucket and load the metadata
        bucket = client.bucket(bucket_name)
        metadata = {'uploaded_by': user.username,
                    'content_type': file.content_type,
                    'size': file.size,
                    'subject': serializer.validated_data['subject']
                    }

        # Upload the file with metadata
        blob = bucket.blob(unique_filename)
        blob.upload_from_string(file.read(),  metadata=metadata)

        # Return a success response
        return Response({'message': 'File uploaded successfully.'}, status=status.HTTP_201_CREATED)
    def get(self, request):
        # Create a Cloud Storage client
        client = storage.Client()

        # Get the bucket
        bucket = client.bucket(bucket_name)
        
        # Get the blobs
        blobs = bucket.list_blobs()
    
        # Return the list of blob names
        return Response([blob.name for blob in blobs], status=status.HTTP_200_OK)

class FileDownloaderView(views.APIView):
    
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        #Get the file name
        file_name = request.query_params.get('file_name')
        if not file_name:
            return Response({'error': 'File name not provided.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a Cloud Storage client
        client = storage.Client()
        
        # Get the bucket
        bucket = client.bucket(bucket_name)
    
        # Get the blob
        blob = bucket.blob(file_name)

        # Download the file content
        file_content = blob.download_as_string()

        # Return FileResponse with attachment
        response = FileResponse(file_content, content_type=blob.content_type)
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'

        return response

class FileSearchView(views.APIView):
    def get(self, request):
        # Extract search term from request (assuming query string)
        file = request.query_params.get('file')

        # Check if search term is provided
        if not file:
            return Response({'error': 'Missing search term parameter'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create a Cloud Storage client
        client = storage.Client()
        
        # Get the bucket
        bucket = client.bucket(bucket_name)

        # List all blobs in the bucket (adjust for filtering based on search term)
        blobs = bucket.list_blobs()

        # Filter results based on search term (implement your logic here)
        filtered_files = [blob.name for blob in blobs if file in blob.name]  # Simple example

        # Return search results
        return Response({'files': filtered_files}, status=status.HTTP_200_OK)