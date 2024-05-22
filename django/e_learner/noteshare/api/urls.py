from django.urls import path
from . import views

urlpatterns = [
    path('resources/', views.ResourceListCreate.as_view(), name='resource-list-create'),
    path('resources/<int:pk>/', views.ResourceDetail.as_view(), name='resource-detail'),
]
