import threading
import time
from pynput import mouse

# this class handles the recording and logging of the mouse input
# it runs as a daemon so it dies with the main thread

class Mouse_monitoring_service (threading.Thread):
	def __init__(self, log):
		# set member variables
		self.m_listener = mouse.Listener(
			on_click = self.on_click,
			on_move=self.on_move,
			on_scroll=self.on_scroll)
		self.log = log
		
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
		self.log.append([time.time(), x, y, button, pressed])
		
	def on_move(self, x, y):
		self.log.append([time.time(), x, y, None, None])
	
	def on_scroll(self, x, y, dx, dy):
		self.log.append([time.time(), dx, dy, "scroll", None])
	
	def clear_log(self):
		self.log = []