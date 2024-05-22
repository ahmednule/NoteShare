from rest_framework import generics, permissions
from .models import Resource
from .serializers import ResourceSerializer
from .permissions import HasPostedResource
from .filters import ResourceFilter
from django_filters.rest_framework import DjangoFilterBackend


class ResourceListCreate(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ResourceFilter

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [permissions.IsAuthenticated]


