# Application definition

BUILTIN_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

PROJECTS_APPS = [
    'ecomm.apps.EcommConfig',
    'elk_search.apps.ElkSearchConfig',
]

INSTALLED_APPS = BUILTIN_APPS + PROJECTS_APPS


