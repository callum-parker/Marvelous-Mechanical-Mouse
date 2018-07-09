from .mouse import Mouse_monitoring_service
from .keyboard import Keyboard_monitoring_service

import threading
import time

# this class manages the keyboard and mouse recorder threads
# it runs as a daemon so it dies with the main thread

class Input_monitoring_service (threading.Thread):
	def __init__(self):
		# set member variables
		self.log = []
		self.mouse_thread = Mouse_monitoring_service(self.log)
		self.keyboard_thead = Keyboard_monitoring_service(self.log)
		
		# init base class
		threading.Thread.__init__(self)
		
		# base class properties
		self.daemon = True
	
	# def run(self):
		# self.start()
	
	def stop(self):
		self.mouse_thread.stop()
		self.keyboard_thead.stop()
		
	def start(self):
		self.mouse_thread.start()
		self.keyboard_thead.start()
		self.run()
	
	def clear_log(self):
		self.log = []