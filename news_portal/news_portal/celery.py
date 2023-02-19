import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_portal.settings')

app = Celery('news_portal')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    # executes every 1 minute
    # 'scraping-task-one-min': {
    #     'task': 'web_interface.tasks.rss_parsing',
    #     'schedule': crontab(),
    # },
    # executes every 15 minutes
    'scraping-task-fifteen-min': {
        'task': 'web_interface.tasks.rss_parsing',
        'schedule': crontab(minute='*/30')
    },
    # # executes daily at midnight
    # 'scraping-task-midnight-daily': {
    #     'task': 'tasks.hackernews_rss',
    #     'schedule': crontab(minute=0, hour=0)
    # }
}