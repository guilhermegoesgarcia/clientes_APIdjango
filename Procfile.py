import gunicorn
import setup

web: gunicorn setup.wsgi
