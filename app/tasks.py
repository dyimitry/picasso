from picasso import app
from app.models import InputFile


@app.task
def processing_file(json_data):
    file = InputFile.objects.get(file=json_data["file"])
    file.processed = True
    file.save()
