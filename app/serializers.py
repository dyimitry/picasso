from rest_framework import serializers
from app.models import InputFile


class InputFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputFile
        fields = ('file', 'uploaded_at', 'processed')
