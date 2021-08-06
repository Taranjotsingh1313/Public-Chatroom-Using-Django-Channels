"""
ASGI config for publicchat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from django.urls import path
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from chat import consumers
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'publicchat.settings')

application = ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(
        AllowedHostsOriginValidator(
            URLRouter(
                [
                    path('ws/public/',consumers.PublicChat.as_asgi())
                ]
            )
        )
    )
})
