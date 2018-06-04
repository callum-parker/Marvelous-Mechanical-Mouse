import threading
from pynput import mouse

# this class handles the recording and logging of the mouse input to STDOUT
# it runs as a daemon so it dies with the main thread

class Mouse_monitoring_service (threading.Thread):
	def __init__(self):
		# set member variables
		self.m_listener = mouse.Listener(on_click = self.on_click)
		self.log = []
		
		# init base class
		threading.Thread.__init__(self)
		
		# base class properties
		self.daemon = True
	
	def run(self):
		m_listener.join()
	
	def stop(self):
		self.m_listener.stop()
		
	def start(self):
		self.m_listener.start()

	def on_click(self, x, y, button, pressed):
		self.log.append([x, y, button, pressed])
	
	def clear_log(self):
		self.log = []