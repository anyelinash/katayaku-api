import paho.mqtt.server as mqtt


def on_connect(client, userdata, flags, rc):
    print(f"Cliente conectado con código de retorno: {rc}")


def on_message(client, userdata, message):
    topic = message.topic
    payload = message.payload.decode('utf-8')
    print(f"Mensaje recibido en el tema '{topic}': {payload}")


def on_subscribe(client, userdata, mid, granted_qos):
    print(f"Cliente se suscribió al tema con éxito")


def on_publish(client, userdata, mid):
    print(f"Mensaje publicado con éxito")


def main():
    broker_address = "localhost"  # Dirección IP o nombre de host de tu servidor MQTT
    port = 1883  # Puerto MQTT predeterminado

    server = mqtt.MQTTServer()
    server.on_connect = on_connect
    server.on_message = on_message
    server.on_subscribe = on_subscribe
    server.on_publish = on_publish

    server.bind(broker_address, port)
    server.start()

    try:
        server.loop_forever()
    except KeyboardInterrupt:
        server.stop()


if __name__ == "__main__":
    main()
