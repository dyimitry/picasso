from celery import shared_task

from picasso import celery_app


@celery_app.task(bind=True, ignore_result=True)
def processing_task(key):
    print(234234)
    return f"task complete {key}"


@shared_task
def add(x, y):
    return x + y
