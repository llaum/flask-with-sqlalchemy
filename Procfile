release: python manage.py db upgrade
worker: celery -A tasks.celery worker --loglevel=info
web: gunicorn wsgi:app --access-logfile=-
