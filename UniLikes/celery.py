import os
import sys

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UniLikes.settings')
app = Celery('stat', broker=settings.CELERY_BROKER_URL)
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
