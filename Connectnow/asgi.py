import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from chat.consumers import ChatConsumer
from public_chat.consumers import PublicChatConsumer
from notification.consumers import NotificationConsumer
from django.urls import path
from decouple import config


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Connectnow.settings')

# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    # Django's ASGI application to handle traditional HTTP requests
    "http": django_asgi_app,

    # WebSocket chat handler
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
         	path('', NotificationConsumer.as_asgi()),
                path('chat/<room_id>/', ChatConsumer.as_asgi()),
                path('public_chat/<room_id>/', PublicChatConsumer.as_asgi()),

            ])
        )
    ),
})
