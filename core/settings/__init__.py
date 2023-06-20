# Settings Folder now is module after created init.py.
from .base import *
from .development import *

# Accessing ENV from .env document by using python-decouple.
# It shouldn't be known by user. so that's why we use this parameter in the .evn file.
ENVIRONMENT = config('ENV')

if ENVIRONMENT=='development':
    from .development import *
else:
    from .production import *