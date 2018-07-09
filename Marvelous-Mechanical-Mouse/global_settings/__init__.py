from .file_handler import Global_settings_file_handler as file_handler

class Global_settings:
	def __init__(self, save_file_location):
		self.save_file_location = save_file_location
		
		self.settings = {}
		self.settings["mouse"] = {}
		self.settings["mouse"]["movement_speed"] = 1
		self.settings["mouse"]["movement_variance"] = 0.025
		self.settings["mouse"]["click_speed"] = 1
		self.settings["mouse"]["click_variance"] = 0.025
		
		self.settings["runtime"] = {}
		self.settings["runtime"]["run_frequency"] = 10.0
		
		if file_handler.exists(save_file_location):
			self.load()
		else:
			self.save()
	
	def save(self):
		file_handler.save(self.save_file_location, self.settings)
	
	def load(self):
		# load the data
		new_settings = file_handler.load(self.save_file_location)
		
		# confirm required sections are present
		assert("mouse" in new_settings)
		assert("movement_speed" in new_settings["mouse"])
		assert("movement_variance" in new_settings["mouse"])
		assert("click_speed" in new_settings["mouse"])
		assert("click_variance" in new_settings["mouse"])
		
		assert("runtime" in new_settings)
		assert("run_frequency" in new_settings["runtime"])
		
		# set the data
		self.settings = new_settings
	