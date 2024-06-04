from django.urls import path
from .views import FileUploadView, FileDownloaderView, FileSearchView

urlpatterns = [
    path('upload/', FileUploadView.as_view()),
    path('download/', FileDownloaderView.as_view()),
    path('search/', FileSearchView.as_view())
]