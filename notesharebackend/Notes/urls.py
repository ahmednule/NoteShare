from django.urls import path
from .views import FileDownloaderView, FileSearchView
from .Db_storage_views import FileUploadView

urlpatterns = [
    path('upload/', FileUploadView.as_view()),
    path('download/', FileDownloaderView.as_view()),
    path('search/', FileSearchView.as_view())
]