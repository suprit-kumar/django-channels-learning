"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from channels.auth import AuthMiddlewareStack
from sock_app.consumers import *
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# application = get_asgi_application()


ws_patterns = [
    path('ws/testcall/',TestConsumer)
]


application = ProtocolTypeRouter({
    # 'http':get_asgi_application(),
    'websocket':AuthMiddlewareStack(URLRouter(ws_patterns)),
})
