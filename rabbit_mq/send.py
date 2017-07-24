#!/usr/bin/env python
import pika
import random
import string
import calendar
import time

NUM_MESSAGES=10

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

for x in range(0, NUM_MESSAGES):
	msg = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))
	messages.append(msg)

times = []

for msgId in range(len(messages)):
	channel.basic_publish(exchange='',
			      routing_key='hello',
			      body=messages[msgId])

	times.append([msgId, calendar.timegm(time.gmtime())])
	#print ("SENT", body)

# Write the current time every time we send a message
f = open('send.log', 'w')
print('Sent ' + str(len(times)) + ' messages')
for item in times:

#	f.write("%s\n" % item)
	msgId = item[0]
	sendTime = item[1] 
	f.write(str(msgId))
	f.write(" ")
	f.write(str(sendTime))
	f.write("\n")

connection.close()
