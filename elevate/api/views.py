from django.shortcuts import render


from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Resource
from .serializers import ResourceSerializer
from .permissions import HasPostedResource

class ResourceListCreateView(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'description']

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [HasPostedResource]
        return super().get_permissions()