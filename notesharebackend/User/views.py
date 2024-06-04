from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets, status
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
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
            
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })           


