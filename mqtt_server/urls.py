# mymqttapp/urls.py
from django.urls import path
from .views import mqtt_connect

urlpatterns = [
    path('mqtt_connect/', mqtt_connect, name='mqtt_connect'),
]
