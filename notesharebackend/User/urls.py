from django.urls import path
from .views import UserViewSet, CustomAuthToken

urlpatterns = [
    path('get_user/<int:id>', UserViewSet.as_view({'get': 'get'})),
     path('api-token-auth/', CustomAuthToken.as_view()),
]