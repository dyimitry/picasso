import os

from celery import Celery

from picasso.settings import CELERY_BROKER_URL, CELERY_RESULT_BACKEND


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "picasso.settings")
celery_app = Celery("picasso")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()

