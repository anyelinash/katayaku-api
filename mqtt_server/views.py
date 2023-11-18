from django.shortcuts import render
import paho.mqtt.client as mqtt
from .mqtt_settings import MQTT_CONFIG

def on_connect(client, userdata, flags, rc):
    print("Conectado al servidor MQTT con código de resultado: " + str(rc))
    for topic in MQTT_CONFIG['mqtt_topics']:
        client.subscribe(topic)

def on_message(client, userdata, msg):
    print("Mensaje recibido en el topic: " + msg.topic)
    print("Mensaje: " + str(msg.payload))

def mqtt_connect(request):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    # Conéctate al servidor MQTT
    client.username_pw_set(MQTT_CONFIG['mqtt_user'], MQTT_CONFIG['mqtt_password'])
    client.connect(MQTT_CONFIG['mqtt_server'], MQTT_CONFIG['mqtt_port'], 60)

    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print("Desconexión del servidor MQTT")
        client.disconnect()

    return render(request, 'mqtt_connected.html')
