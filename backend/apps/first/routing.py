from django.urls import path

from apps.first.consumer import CarConsumer

websocket_urlpatterns = [
    path('', CarConsumer.as_asgi())
]