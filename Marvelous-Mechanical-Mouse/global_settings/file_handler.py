import os
import re
import configparser

class Global_settings_file_handler:
	@staticmethod
	def save(location, data):
		# construct the data to save
		config = configparser.ConfigParser()
		for section in data:
			config[section] = data[section]
		
		# save the data
		with open(location, "w") as configfile:
			config.write(configfile)
	
	@staticmethod
	def load(location):
		# load the configuration data
		config = configparser.ConfigParser()
		config.read(location)
		
		# construct type checking
		match_string_float = "^\d*?\.\d+?$"
		match_string_int = "^\d+?$"
		
		# construct a dictionary to store it in
		config_dictionary = {}
		for section in config.sections():
			config_dictionary[section] = {}
			
			for attribute in config[section]:
				# check attribute type against valid patterns
				if not re.match(match_string_float, config[section][attribute]) is None: # float
					new_attribute = float(config[section][attribute])
				
				elif not re.match(match_string_int, config[section][attribute]) is None: # int
					new_attribute = int(config[section][attribute])
				
				else: # string as default
					new_attribute = config[section][attribute]
				
				# set the attribute
				config_dictionary[section][attribute] = new_attribute
		
		# return the dictionary
		return config_dictionary
	
	@staticmethod
	def exists(location):
		return os.path.isfile(location)