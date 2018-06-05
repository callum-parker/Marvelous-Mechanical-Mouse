import threading
import random
from time import sleep
from pynput import mouse

# i should split this class into two; one for macros, one for mouse control

class Mouse_controller (threading.Thread):
	def __init__(self, log, motion_speed, motion_variance, click_speed, click_variance):
		# set member variables
		self.mouse_controller = mouse.Controller()
		self.action_list = log
		
		self.motion_speed = motion_speed
		self.motion_variance = motion_variance
		self.click_speed = click_speed
		self.click_variance = click_variance
		
		# init base class
		threading.Thread.__init__(self)
		
		# base class properties
		self.daemon = True

	
	def run(self):
		for action in self.action_list:
			if action["action"] == None:
				self.move_to(action["x"], action["y"])
				sleep(self.motion_speed + (random.random() * self.motion_variance))
			else:
				self.move_to(action["x"], action["y"])
				self.do_click(action["action"])
				sleep(self.click_speed + (random.random() * self.click_variance))
		
	def do_click(self, button):
		self.mouse_controller.press(button)
		self.mouse_controller.release(button)
		
	def move_to(self, x, y):
		self.mouse_controller.position = (x, y)