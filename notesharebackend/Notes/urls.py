from django.urls import path
from .views import UploadFileView, ResourceListView, ResourceSearchView

urlpatterns = [
    path('upload/', UploadFileView.as_view(), name='upload-file'),
    path('resources/', ResourceListView.as_view(), name='resource-list'),
    path('search/', ResourceSearchView.as_view(), name='resource-search'),
]
