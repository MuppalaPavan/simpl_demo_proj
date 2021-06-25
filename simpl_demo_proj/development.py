from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3_psycopg2',
        'NAME': 'honeybee_dev',
        'USER': 'sqlite3',
        'PASSWORD': 'sqlite3',
        'HOST': 'db',
        # 'HOST': '3.6.98.0',
        'PORT': '5432',
    }
}

FrontEndUrl = 'superflex.appiness.co.in'
FED_BD_URL = 'bdflex.appiness.co.in'
FED_ADMIN_URL = 'adminflex.appiness.cc'
FED_RECRUITER_URL = 'recruitflex.appiness.co.in'
BACKEND_URL = 'honeybee.appinessworld.com'

FCM_SERVER_KEY = 'AAAA5sxYz8w:APA91bFEwIFRiMuj5yQJH4wIx8SaOCF_0Tt3tlZgH9S8KpZvEZA2rsxdc80iApmvehOD-0tqZ_u8RnKp7toJTrbysG4-QU-hdAn-esDa7uXEHKi6qutY6wThJBrOFLIdvclyQyIiHvtF'
