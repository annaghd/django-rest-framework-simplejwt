from __future__ import unicode_literals

from .backends import TokenBackend
from .settings import api_settings
from django.conf import settings
from django.apps import apps as django_apps

User = django_apps.get_model(settings.JWT_AUTH_USER_MODEL, require_ready=False)
token_backend = TokenBackend(api_settings.ALGORITHM, api_settings.SIGNING_KEY,
                             api_settings.VERIFYING_KEY, api_settings.AUDIENCE, api_settings.ISSUER)
