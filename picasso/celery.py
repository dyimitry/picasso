import os

from celery import Celery

from picasso.settings import CELERY_BROKER_URL, CELERY_RESULT_BACKEND


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "picasso.settings")

app = Celery("picasso", broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
