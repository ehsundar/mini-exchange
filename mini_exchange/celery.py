import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mini_exchange.settings")

app = Celery("mini_exchange")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.setdefault("broker_connection_retry_on_startup", True)
app.autodiscover_tasks()
