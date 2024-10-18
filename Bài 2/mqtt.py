import json
import time
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "custom-topic"

data = {
    "student-id": 5578,
    "name": "hieunt",
    "id": 11,
    "packet_no": 126,
    "temperature": 100,
    "humidity": 60,
    "tds": 1100,
    "pH": 5.0
}

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic: {msg.topic}")

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

client.loop_start()

while True:
    json_data = json.dumps(data)
    client.publish(TOPIC, json_data)
    print(f"Published: {json_data} to topic: {TOPIC}")
    time.sleep(10)  

client.loop_stop()
client.disconnect()