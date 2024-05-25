from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets, status
from rest_framework.views import APIView
from .models import User
from .serialisers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    #queryset = User.objects.all()
    #serializer_class = UserSerializer
    def get(self, request, id=None):
        # Filter user by primary key (pk)
            try:
                user = User.objects.get(id=id)
                if user:
                    serializer = UserSerializer(user)
                    return JsonResponse(serializer.data, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return JsonResponse({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)



