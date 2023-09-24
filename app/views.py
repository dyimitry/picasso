from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import InputFile
from .serializers import InputFileSerializer


class ApiLoadFiles(APIView):

    def post(self, request):
        uploaded_file = request.FILES.get('file')

        if not uploaded_file:
            return Response({'error': 'No file data'}, status=status.HTTP_400_BAD_REQUEST)

        input_file = InputFile(file=uploaded_file)
        input_file.save()

        return Response({'message': 'File uploaded successfully'}, status=status.HTTP_200_OK)

    def get(self, request):
        files = InputFile.objects.all()
        serializer = InputFileSerializer(files, many=True)
        return Response(serializer.data)
