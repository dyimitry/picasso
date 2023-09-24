from rest_framework import serializers
from app.models import InputFile


class InputFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputFile
        # Указываем поля модели, с которыми будет работать сериализатор;
        # поля модели, не указанные в перечне, сериализатор будет игнорировать.
        # Для перечисления полей можно использовать список или кортеж.
        fields = ('file', 'uploaded_at', 'processed')
