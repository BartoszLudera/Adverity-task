
from django.contrib import admin
from .models import UploadedFile

class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ['file', 'uploaded_at', 'created_by', 'json_data_display']

    def json_data_display(self, obj):
        import json
        return json.dumps(obj.json_data, indent=2)  

    json_data_display.short_description = 'JSON Data'

admin.site.register(UploadedFile, UploadedFileAdmin)
