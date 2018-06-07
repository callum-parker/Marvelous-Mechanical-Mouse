import threading
import time
from pynput import keyboard

# this class handles the recording and logging of the keyboard input
# it runs as a daemon so it dies with the main thread

class Keyboard_monitoring_service (threading.Thread):
	def __init__(self, log):
		# set member variables
		self.kb_listener = keyboard.Listener(
			on_press=self.on_press,
			on_release=self.on_release)
		self.log = log
		
		# init base class
		threading.Thread.__init__(self)
		
		# base class properties
		self.daemon = True
	
	def run(self):
		kb_listener.join()
	
	def stop(self):
		self.kb_listener.stop()
		
	def start(self):
		self.kb_listener.start()
	
	def on_press(self, key):
		self.log.append([time.time(), None, None, key, True])
		
	def on_release(self, key):
		self.log.append([time.time(), None, None, key, False])
	