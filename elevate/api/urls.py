# api/urls.py

from django.urls import path
from .views import ResourceListCreateView

urlpatterns = [
    path('resources/', ResourceListCreateView.as_view(), name='resource-list-create'),
]
