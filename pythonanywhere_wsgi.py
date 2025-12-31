"""
WSGI config for blog_main project on PythonAnywhere.

This module contains the WSGI application used by PythonAnywhere.
"""

import os
import sys

# Add your project directory to the sys.path
# IMPORTANT: Replace 'YOUR_USERNAME' with your actual PythonAnywhere username
path = '/home/YOUR_USERNAME/MasthiUpdatesWebsite'
if path not in sys.path:
    sys.path.insert(0, path)

# Set environment variable for Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'blog_main.settings'

# Activate your virtual environment
# This is handled automatically by PythonAnywhere when you set the virtualenv path

# Import Django's WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
