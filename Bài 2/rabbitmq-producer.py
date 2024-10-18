import json
import pika
import time


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

queue_name = 'sensor_data'
channel.queue_declare(queue=queue_name)

data = {
    "student-id": 5578,
    "name": "hieunt",
    "id": 11,
    "packet_no": 126,
    "temperature": 30,
    "humidity": 60,
    "tds": 1100,
    "pH": 5.0,
    "timestamp": time.time()
}


while True:
    json_data = json.dumps(data)
    channel.basic_publish(exchange='', routing_key=queue_name, body=json_data)
    print(f"Sent: {json_data}")
    time.sleep(10) 


connection.loop_stop()
connection.close()