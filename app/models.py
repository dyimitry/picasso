from django.db import models

from picasso.settings import APP_FILES_ROOT

class InputFile(models.Model):
    file = models.FileField(upload_to=APP_FILES_ROOT)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
