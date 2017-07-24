#!/usr/bin/env python

import random
import string
import calendar
import time
import sys
import stomp

NUM_MESSAGES=10

conn = stomp.Connection10()
 
conn.start()
 
conn.connect()
 
messages = []

for x in range(0, NUM_MESSAGES):
	msg = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(15))
	messages.append(msg)

times = []

for msgId in range(len(messages)):
	conn.send('SampleQueue', messages[msgId])

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

conn.disconnect()
