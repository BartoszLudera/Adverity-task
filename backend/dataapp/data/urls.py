from django.urls import path
from .views import UploadedFileList, UploadedFileDetail

urlpatterns = [
    path('files/', UploadedFileList.as_view(), name='uploadedfile-list'),
    path('files/<int:pk>/', UploadedFileDetail.as_view(), name='uploadedfile-detail'),
]
