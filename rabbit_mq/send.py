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
	#connection = pika.BlockingConnection(pika.ConnectionParameters(host='ugster09.student.cs.uwaterloo.ca'))

channel = connection.channel()

channel.queue_declare(queue='hello')

for x in range(0, 10000):
	body = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))
	channel.basic_publish(exchange='',
			      routing_key='hello',
			      body=body)

#print ("SENT", body)
connection.close()
