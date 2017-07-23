#!/usr/bin/env python
import pika
import random
import string

credentials = pika.PlainCredentials('guest', 'guest')
params = pika.ConnectionParameters(
	host='ugster09',
	port=5672,
	virtual_host='/',
	credentials=credentials
	)
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='hello')

messages = []

for x in range(0, 100000):
	msg = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))
	messages.append(msg)

for i in range(len(messages)):
	channel.basic_publish(exchange='',
			      routing_key='hello',
			      body=messages[i])

#print ("SENT", body)
connection.close()
