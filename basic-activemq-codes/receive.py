import stomp
import time
import sys
import calendar
 
class SampleListener(object):
  def on_message(self, headers, msg):
    print(msg)
 
conn = stomp.Connection10()
 
conn.set_listener('SampleListener', SampleListener())
 
conn.start()
 
conn.connect()
 
conn.subscribe('SampleQueue')
 
time.sleep(1) # secs
 
conn.disconnect()
