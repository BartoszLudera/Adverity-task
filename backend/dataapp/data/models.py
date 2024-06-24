# csv_app/models.py
from django.db import models
from django.conf import settings
import pandas as pd
import io

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='items', on_delete=models.CASCADE)
    json_data = models.JSONField(default=dict, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk: 
            super().save(*args, **kwargs)
            self.parse_csv()
        super().save(*args, **kwargs)

    def parse_csv(self):
        if self.file:
            self.file.seek(0)  
            csv_file = self.file.read().decode('utf-8')
            data = pd.read_csv(io.StringIO(csv_file))
            self.json_data = data.to_dict(orient='records')
