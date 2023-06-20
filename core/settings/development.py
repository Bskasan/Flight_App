from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE = [
    # Extras;
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]
