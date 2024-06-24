# csv_app/serializers.py
from rest_framework import serializers
from .models import UploadedFile

class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ['id', 'file', 'uploaded_at', 'created_by', 'json_data']
        read_only_fields = ['json_data']  
