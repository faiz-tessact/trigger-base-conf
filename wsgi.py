import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Container')

from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()