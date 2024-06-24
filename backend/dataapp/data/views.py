# csv_app/views.py
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from .models import UploadedFile
from .serializers import UploadedFileSerializer

class UploadedFileList(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request):
        data = request.data.copy()
        data['created_by'] = request.user.id
        file_serializer = UploadedFileSerializer(data=data)
        if file_serializer.is_valid():
            file_instance = file_serializer.save()
            file_instance.parse_csv()
            file_instance.save(update_fields=['json_data'])
            return Response(UploadedFileSerializer(file_instance).data, status=status.HTTP_201_CREATED)
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        files = UploadedFile.objects.all()
        serializer = UploadedFileSerializer(files, many=True)
        return Response(serializer.data)

class UploadedFileDetail(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        return get_object_or_404(UploadedFile, pk=pk)

    def get(self, request, pk):
        file_instance = self.get_object(pk)
        serializer = UploadedFileSerializer(file_instance)
        return Response(serializer.data)

    def delete(self, request, pk):
        file_instance = self.get_object(pk)
        file_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
