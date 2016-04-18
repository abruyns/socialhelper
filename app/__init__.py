from flask import Flask
from .utils import make_celery
 

app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile('config.py')


#Celery initialization
celery = make_celery(app)

from app import views
