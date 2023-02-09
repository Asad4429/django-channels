"""
ASGI config for testchannels project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from test.consumers import TestConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testchannels.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter([
        path('practice', TestConsumer.as_asgi())
    ])
})
