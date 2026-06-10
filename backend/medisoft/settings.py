from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-^x+bwnq6y7h5tb40ln%8b_s%xud&m@(%#9c#tsz&(mp7k9seu^'


DEBUG = True

ALLOWED_HOSTS = ['*']



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'core',
]

AUTH_USER_MODEL = 'core.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'medisoft.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'medisoft.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'medisoft.backends.mysql',
        'NAME': 'medisoft',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}




AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


LOGIN_URL = '/api/auth/login/'

CORS_ALLOW_ALL_ORIGINS = True


BKASH = {
    'app_key': '',
    'app_secret': '',
    'username': 'sandbox',
    'password': 'sandbox',
    'sandbox': True,
    'success_url': 'http://localhost:5173/payments/success',
    'fail_url': 'http://localhost:5173/payments/fail',
    'cancel_url': 'http://localhost:5173/payments/cancel',
    'ipn_url': 'http://127.0.0.1:8000/api/payments/bkash/ipn/',
}

BKASH_API = {
    'sandbox': {
        'base': 'https://sandbox.pay.bkauniv.com/merchantained/v1.2.0-beta',
        'grant_token': '/tokenized/checkout/grant/token',
        'create_payment': '/tokenized/checkout/create',
        'query_payment': '/tokenized/checkout/payment/status',
        'refund': '/tokenized/checkout/payment/refund',
    },
    'production': {
        'base': 'https://tokenized.pay.bkauniv.com/merchantained/v1.2.0-beta',
        'grant_token': '/tokenized/checkout/grant/token',
        'create_payment': '/tokenized/checkout/create',
        'query_payment': '/tokenized/checkout/payment/status',
        'refund': '/tokenized/checkout/payment/refund',
    },
}

SERVICE_DEFAULT_PRICES = {
    'Appointment': 500.00,
    'SeatBooking': 1500.00,
    'MedicineOrder': 0.00,
    'LabBooking': 800.00,
    'Ambulance': 1200.00,
}
