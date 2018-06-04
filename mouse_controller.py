import threading
from time import sleep
from pynput import mouse

# i should split this class into two; one for macros, one for mouse control

class Mouse_controller (threading.Thread):
	def __init__(self, log):
		# set member variables
		self.mouse_controller = mouse.Controller()
		self.action_list = log
		
		# init base class
		threading.Thread.__init__(self)
		
		# base class properties
		self.daemon = True

	
	def run(self):
		for action in self.action_list:
			self.move_to(action["x"], action["y"])
			self.do_click(action["action"])
			sleep(.1) # i should make this configurable at some point
		
	def do_click(self, button):
		self.mouse_controller.press(button)
		self.mouse_controller.release(button)
		
	def move_to(self, x, y):
		self.mouse_controller.position = (x, y)