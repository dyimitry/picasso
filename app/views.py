from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app.models import InputFile
from app.serializers import InputFileSerializer
from app.tasks import processing_task


class ApiLoadFiles(APIView):

    def post(self, request):
        uploaded_file = request.FILES.get('file')

        if not uploaded_file:
            return Response({'error': 'No file data'}, status=status.HTTP_400_BAD_REQUEST)

        input_file = InputFile(file=uploaded_file)
        input_file.save()

        # send to celery
        task = processing_task.delay()

        return Response({'message': 'File uploaded successfully'}, status=status.HTTP_201_CREATED)

    def get(self, request):
        files = InputFile.objects.all()
        serializer = InputFileSerializer(files, many=True)

        return Response(serializer.data)
