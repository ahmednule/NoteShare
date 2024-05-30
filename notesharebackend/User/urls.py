from django.urls import path, include
from .views import UserViewSet, register_user
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('get_user/<int:id>', UserViewSet.as_view({'get': 'get'})),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('register/', register_user, name='register_user'),
]