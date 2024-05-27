from django.urls import path
from .views import UserViewSet

urlpatterns = [
    path('get_user/<int:id>', UserViewSet.as_view({'get': 'get'})),
]