import threading
from keybind_detector import Keybind_detector
from keybind_detector.keybind_book.keybind_book_factory import Keybind_book_factory
# i need to import the actual completed keybinding package in here

# it runs as a daemon so it dies with the main thread

class Keybind_manager (threading.Thread):
	def __init__(self, save_file_location, callback, macros):
		# init base class
		threading.Thread.__init__(self)
		
		# set member variables
		self.callback = callback
		self.save_file_location = save_file_location
		self.monitoring_thread = Keybind_detector(
			self.keybind_callback,
			self.save_file_location)
		
		# make sure all default macros are present
		# self.monitoring_thread.keybind_list is our data manager
		for macro in macros:
			keybinding = Keybind_book_factory.key_combination(macro[0])
			if not self.monitoring_thread.keybind_list.has(keybinding):
				self.monitoring_thread.keybind_list.create_keybind(macro)
				# self.monitoring_thread.keybind_list.save()
		
		# base class properties
		self.daemon = True
	
	def run(self):
		self.monitoring_thread.start()
		# self.monitoring_thread.keybind_list.save()
		self.monitoring_thread.join()
		
	def is_active(self):
		return self.monitoring_thread.is_active()
	
	def stop(self):
		self.monitoring_thread.stop()
	
	def keybind_callback(self, keybind):
		self.callback(keybind["event"], keybind["data"])
	