from .file_handler import Macro_book_file_handler as file_handler
from .factory import Macro_factory

class Macro_book:
	def __init__(self, save_file_location):
		self.save_file_location = save_file_location
		
		self.macro_list = {}

		
		if file_handler.exists(save_file_location):
			self.load()
		else:
			self.save()
	
	def save(self):
		file_handler.save(self.save_file_location, self.macro_list)
	
	def load(self):
		# load the data
		new_macro_list = file_handler.load(self.save_file_location)
		
		# confirm data is valid

		
		# set the data
		self.macro_list = new_macro_list
	
	def add(self, id, macro):
		self.macro_list[id] = macro
	
	def remove(self, macro_id):
		if macro_id in self.macro_list:
			del self.macro_list[macro_id]
	
	def get(self, id):
		if id in self.macro_list:
			return self.macro_list[id]
		else:
			raise ValueError
	
	def set(self, id, macro):
		# do some type checking
		self.macro_list[id] = macro
	
	@staticmethod
	def construct_macro(macro_data):
		new_record = Macro_factory.record(macro_data)
		return new_record