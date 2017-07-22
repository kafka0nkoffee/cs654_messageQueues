#!/usr/bin/env python
import pika

#connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
credentials = pika.PlainCredentials('guest', 'guest')
params = pika.ConnectionParameters('ugster08.student.cs.uwaterloo.ca', 5672, '/', credentials)
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(body)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
