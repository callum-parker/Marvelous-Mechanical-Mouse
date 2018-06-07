from action_factory import Action_factory as af
import threading
import random
import pynput
from time import sleep

class Output_controller (threading.Thread):
	def __init__(self, log, motion_speed, motion_variance, click_speed, click_variance):
		# set member variables
		self.mouse_controller = pynput.mouse.Controller()
		self.keyboard_controller = pynput.keyboard.Controller()
		
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
		speed = 1.0
		variance = 0.0
		for record in self.action_list:
			if record["action"] is af.Action.move:
				(x, y) = (record["position"]["x"], record["position"]["y"])
				self.move_to(x, y)
				speed = self.motion_speed
				variance = random.random() * self.motion_variance
				
			if record["action"] is af.Action.mouse_click:
				if record["pressed"] == True:
					self.press_button(record["button"])
				else:
					self.release_button(record["button"])
				speed = self.click_speed
				variance = random.random() * self.click_variance
				
			if record["action"] is af.Action.scroll: # buggy, recorded but doesnt work properly
				(x, y) = (record["direction"]["x"], record["direction"]["y"])
				self.scroll(x, y)
				#maybe should separate this into its own setting
				speed = self.click_speed
				variance = random.random() * self.click_variance
			
			if record["action"] is af.Action.keypress:
				if record["pressed"] == True:
					self.press_key(record["key"])
				else:
					self.release_key(record["key"])
				#maybe should separate this into its own setting
				speed = self.click_speed
				variance = random.random() * self.click_variance
			
			sleep((record["time"] / speed) + variance)
		
	def press_button(self, button):
		self.mouse_controller.press(button)
		
	def release_button(self, button):
		self.mouse_controller.release(button)
		
	def move_to(self, x, y):
		self.mouse_controller.position = (x, y)
	
	def scroll(self, x, y):
		self.mouse_controller.scroll(x, y)
	
	def press_key(self, key):
		self.keyboard_controller.press(key)
	
	def release_key(self, key):
		self.keyboard_controller.release(key)