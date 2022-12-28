
import os
from api.routing import websocket_urlpatterns as websocket_url
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bindu_server.settings')

app = get_asgi_application()

application = ProtocolTypeRouter({
    'http': app,
    'websocket': AllowedHostsOriginValidator(AuthMiddlewareStack(URLRouter(websocket_url)))
})
