from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view

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




@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'},
                        status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password, email=email)
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=status.HTTP_201_CREATED)
