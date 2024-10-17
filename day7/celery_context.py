from celery import Task
from app import create_app

app_instance, _ = create_app()

class appContext(Task):
    def __call__(self, *args, **kwargs):
        with app_instance.app_context():
            return Task.__call__(self, *args, **kwargs)