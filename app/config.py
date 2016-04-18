import os
# General Flask app settings
#DEBUG = os.environ.get('DEBUG', None)
WTF_CSRF_ENABLED = True
SECRET_KEY = "you will never guess"
#COUPON_SAVE_DIR = os.environ.get('COUPON_SAVE_DIR', None)
#QUALIFIED_MEDIA_URL = os.environ.get('QUALIFIED_MEDIA_URL', None)
 
# Twilio API credentials
TWILIO_ACCOUNT_SID = "AC101de8b435bfc33ed8615029baff8eb8"
TWILIO_AUTH_TOKEN = "42a4770c23a285a0bb6f67bd63fca925"
TWILIO_NUMBER = "+16504498498"

#Celery
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'