"""
WSGI config for tst_a066a238_ba78_4cb_156 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "tst_a066a238_ba78_4cb_156.settings"
)

application = get_wsgi_application()
