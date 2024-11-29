from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
app = Celery('demo')

app.conf.update(
    task_cuncurrency=1,
    worker_prefetch_multiplier=1
)

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
