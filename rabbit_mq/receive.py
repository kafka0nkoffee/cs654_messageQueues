#!/usr/bin/env python
import pika
import calendar
import time
import sys

NUM_MESSAGES=10

msgId=0
f = open('receive.log', 'w')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
	global msgId
	global times
	global f

	times.append([msgId,calendar.timegm(time.gmtime())])
	msgId+=1

	# Stopping conditions
	if msgId==NUM_MESSAGES:

		print('Received ' + str(len(times)) + ' messages')
		for item in times:
			
			msgId = item[0]
			receiveTime = item[1] 
			f.write(str(msgId))
			f.write(" ")
			f.write(str(receiveTime))
			f.write("\n")

		print("Done consuming.")
		sys.exit()

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')

times = []
channel.start_consuming()
