import os
import pickle

class Macro_book_file_handler:
	@staticmethod
	def save(location, data):
		with open(location, 'wb') as file:
			pickle.dump(data, file)
	
	@staticmethod
	def load(location):
		data = {}
		with open(location, 'rb') as file:
			data = pickle.load(file)
		return data
	
	@staticmethod
	def exists(location):
		return os.path.isfile(location)