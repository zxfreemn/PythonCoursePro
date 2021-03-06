# файл receive.py

import pika
import time
import random

NAME = 'Logger 2'

connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='topic')
queue_name = 'hello_3'
result = channel.queue_declare(queue=queue_name, exclusive=False)
channel.queue_bind(exchange='logs', routing_key='*.bye', queue=queue_name)


def callback(ch, method, properties, body):
    print(f'Processing msg {body.decode()} by: {NAME}')
    channel.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=queue_name,
                      on_message_callback=callback,
                      auto_ack=False)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
