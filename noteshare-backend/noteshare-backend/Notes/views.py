from django.shortcuts import render


from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Notes
from .serializers import NotesSerializer
from .permissions import HasPostedResource

class ResourceListCreateView(generics.ListCreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'description']

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [HasPostedResource]
        return super().get_permissions()