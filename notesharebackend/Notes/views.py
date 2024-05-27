from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Resource, UserUpload
from .serializers import ResourceSerializer, UserUploadSerializer
from django.contrib.auth.models import User

class UploadFileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = UserUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ResourceListView(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_upload = UserUpload.objects.filter(user=self.request.user).exists()
        if user_upload:
            return Resource.objects.all()
        return Resource.objects.none()

class ResourceSearchView(generics.ListAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_upload = UserUpload.objects.filter(user=self.request.user).exists()
        if user_upload:
            return Resource.objects.all()
        return Resource.objects.none()
