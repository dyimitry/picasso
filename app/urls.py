from django.urls import path
from app.views import ApiLoadFiles

urlpatterns = [
    path("upload/", ApiLoadFiles.as_view()),
]