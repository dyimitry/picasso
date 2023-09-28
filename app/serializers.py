from rest_framework import serializers
from app.models import InputFile


class InputFileSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()

    class Meta:
        model = InputFile
        fields = ('file', 'uploaded_at', 'processed')

    def get_file(self, obj):
        return obj.file.name
