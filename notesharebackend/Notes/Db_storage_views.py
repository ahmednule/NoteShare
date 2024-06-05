# fileapp/views.py

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import HttpResponse
from .models import File
from rest_framework.permissions import IsAuthenticated
from .serializers import FileUploadSerializer, FileRetrieveSerializer

class FileUploadView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileUploadSerializer
    parser_classes = [MultiPartParser, FormParser]
    #permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        file = request.FILES['file']
        file_instance = File(filename=file.name, content=file.read(), user=request.user, subject=request.subject)
        file_instance.save()
        serializer = self.get_serializer(file_instance)
        return Response({'message': 'File uploaded successfully.'}, status=status.HTTP_201_CREATED)

class FileRetrieveView(generics.RetrieveAPIView):
    queryset = File.objects.all()
    serializer_class = FileRetrieveSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        response = HttpResponse(instance.content, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{instance.filename}"'
        return response
