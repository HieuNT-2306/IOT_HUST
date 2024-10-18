import json
import pika
from datetime import datetime

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

queue_name = 'sensor_data'
channel.queue_declare(queue=queue_name)

def callback(ch, method, properties, body):
    data = json.loads(body)
    timestamp = datetime.fromtimestamp(data['timestamp'])
    print("Received data:")
    print(f"ID: {data['id']}")
    print(f"Student ID: {data['student-id']}")
    print(f"Name: {data['name']}")
    print(f"Packet No: {data['packet_no']}")
    print(f"Temperature: {data['temperature']} °C")
    print(f"Humidity: {data['humidity']} %")
    print(f"TDS: {data['tds']} mg/L")
    print(f"pH: {data['pH']}")
    print(f"Timestamp: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()