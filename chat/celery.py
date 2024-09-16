import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat.settings')

app = Celery('chat')

# Load task settings from Django settings with 'CELERY_' namespace
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically discover tasks in your installed apps
app.autodiscover_tasks()

# Celery beat schedule configuration
app.conf.beat_schedule = {
    'process-task-queue': {
        'task': 'app.tasks.process_task_queue',
        'schedule': 30.0,  # run every 30 seconds
    },
    'check-completed-tasks': {
        'task': 'app.tasks.check_completed_tasks',
        'schedule': crontab(minute='*/10'),  # run every 10 minutes
    },
}
