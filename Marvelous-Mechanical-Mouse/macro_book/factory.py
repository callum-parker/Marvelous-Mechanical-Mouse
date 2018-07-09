import sys
import os
import pynput
import uuid
from enum import Enum, auto

class Macro_factory:
	class Action (Enum):
		move = auto()
		mouse_click = auto()
		scroll = auto()
		keypress = auto()
	
	@staticmethod
	def record(log):
		data = Macro_factory.parse_log(log)
		new_record = {"id": str(uuid.uuid4()), "data": data}
		return new_record
	
	@staticmethod
	def parse_log(log):
		# the returned data structure has the following specification:
		#
		#	a list object, containing a series of dictionary objects.
		#
		#	all records within this structure are comprised of a time difference between
		#	each record and the following one, an Action enum type and a list of associated
		#	data. this data depends on the type ofaction, and is to behandled as different
		#	cases.
		#
		#
		# incoming data begins with a timestamp and x and y co-ords, followed by the action
		# and the button state if applicable.
		
		action_list = []
		last_time = log[0][0]
		
		for i in range(0, len(log)-2):
			new_record = {}
			
			time = log[i+1][0]
			new_record["time"] = time - last_time
			last_time = time
			
			if log[i][3] == None and log[i][4] == None: # movement only
				new_record["action"] = Macro_factory.Action.move
				new_record["position"] = {'x' : log[i][1], 'y' : log[i][2]}
				
			elif type(log[i][3]) is pynput.mouse.Button: # a mouse click
				new_record["action"] = Macro_factory.Action.mouse_click
				new_record["button"] = log[i][3]
				new_record["pressed"] = log[i][4]
				
			elif log[i][3] == "scroll": # scroll
				new_record["action"] = Macro_factory.Action.scroll
				new_record["direction"] = {'x' : log[i][1], 'y' : log[i][2]}
				
			elif type(log[i][3]) is pynput.keyboard.Key or type(log[i][3]) is pynput.keyboard.KeyCode: # keypress
				new_record["action"] = Macro_factory.Action.keypress
				new_record["key"] = log[i][3]
				new_record["pressed"] = log[i][4]
				
			else:
				print("Offending record: " + str(log[i]))
				raise Exception("unknown data type recieved for log processing")
			
			action_list.append(new_record)
		return action_list
			
			# old data structure code
			# if log[i][3] == True or log[i][3] == None: # only record one click action from the two records of it
				# new_record = {}
				# new_record["x"] = log[i][0]
				# new_record["y"] = log[i][1]
				# new_record["action"] = log[i][2]