import sys
import threading

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

from .dialogs.main_window import Ui_MainWindow as Main_window_ui
from .settings_window import Settings_window

from global_settings import Global_settings
from keybind_manager import Keybind_manager
from macro_book import Macro_book
from services.monitoring import Input_monitoring_service
from services.output import Output_controller

class Main_window (QMainWindow, Main_window_ui):
	# ui macro data
	# pynput uses ascii control codes to represent certain key combinations
	builtin_macros = [
		[("\x12", "ctrl_l"), "ui_action_invoke", ["run_once"]]
	]
	def __init__(self):
		super(Main_window, self).__init__()
		
		# set class data and objects
		self.keybind_file_location = "var/default.keybindings"
		self.settings_save_file_location = "var/settings.ini"
		self.macro_file_location = "var/default.macros"
		
		self.timer = None
		
		self.default_current_macro = {"id": None, "data": []}
		self.current_macro = self.default_current_macro
		
		self.settings_manager = Global_settings(self.settings_save_file_location)
		
		self.keybind_service = Keybind_manager(
			self.keybind_file_location,
			self.keybind_callback,
			self.builtin_macros)
		
		self.macro_manager = Macro_book(self.macro_file_location)
		
		# these are set at run time as needed
		self.monitoring_service = None
		self.output_service = None
		
		self.settings_window = None
		self.save_as_window = None
		self.open_window = None
		
		# set up GUI
		self.setupUi(self)
		
		# connect buttons
		self.widget_button_stop_running.clicked.connect(self.stop_running)
		self.widget_button_start_running.clicked.connect(self.start_running)
		self.widget_button_run_once.clicked.connect(self.run_once)
		self.widget_button_save_recording.clicked.connect(self.save_recording)
		self.widget_button_clear_recording.clicked.connect(self.clear_recording)
		self.widget_button_stop_recording.clicked.connect(self.stop_recording)
		self.widget_button_start_recording.clicked.connect(self.start_recording)
		
		# connect menu bar buttons
		# file
		self.action_open.triggered.connect(self.menu_file_open)
		self.action_save.triggered.connect(self.menu_file_save)
		self.action_save_as.triggered.connect(self.menu_file_save_as)
		self.action_quit.triggered.connect(self.menu_file_quit)
		#settings
		self.action_playback_settings.triggered.connect(self.menu_settings_playback_settings)
		
		# connect list display
		self.widget_macros_list.itemActivated.connect(self.macros_list_selected)
		
		# start the services
		self.keybind_service.start()
		
		# update the UI
		self.update_ui_elements()
		
	# button methods
	def stop_running(self):
		self.stop_timer()
		
	def start_running(self):
		self.start_timer()
		
	def run_once(self):
		if not len(self.current_macro) < 1:
			self.output_service = Output_controller(
				self.current_macro["data"],
				self.settings_manager.settings)
			
			self.output_service.start()
			self.output_service.join()
		
			# clean up after
			self.output_service = None
		
	def save_recording(self):
		self.macro_manager.add(self.current_macro["id"], self.current_macro["data"])
		self.update_list_gui()
		
	def clear_recording(self):
		self.current_macro = self.default_current_macro
		self.update_log_gui()
		
	def stop_recording(self):
		if self.monitoring_service != None:
			self.monitoring_service.stop()
			self.update_log()
			self.update_log_gui()
		
	def start_recording(self):
		self.monitoring_service = Input_monitoring_service()
		self.monitoring_service.start()
	
	# menu bar methods
	# file
	def menu_file_open(self):
		options = QFileDialog.Options()
		file_name, _ = QFileDialog.getOpenFileName(
			self,
			"Open file",
			"",
			"Macro Pickle Files (*.macros)",
			options = options)
		if file_name:
			self.macro_file_location = file_name
			self.macro_manager.save_file_location = self.macro_file_location
			self.macro_manager.load()
			self.update_ui_elements()
	
	def menu_file_save(self):
		self.macro_manager.save()
	
	def menu_file_save_as(self):
		options = QFileDialog.Options()
		file_name, _ = QFileDialog.getSaveFileName(
			self,
			"Save as",
			"",
			"Macro Pickle Files (*.macros)",
			options = options)
		if file_name:
			self.macro_file_location = file_name
			self.macro_manager.save_file_location = self.macro_file_location
			self.macro_manager.save()
	
	def menu_file_quit(self):
		quit()
	
	# settings
	def menu_settings_playback_settings(self):
		self.settings_window = Settings_window(self.settings_manager)
		self.settings_window.show()
	
	# list widget methods
	def macros_list_selected(self):
		for item in self.widget_macros_list.selectedItems():
			id = item.text()
			self.current_macro = {"id": id, "data": self.macro_manager.get(id)}
			self.update_log_gui()
	
	# methods related to data management and processing
	def update_log(self):
		new_record = self.macro_manager.construct_macro(self.monitoring_service.log)
		self.current_macro = new_record
	
	# methods relating to presentation of data
	def update_ui_elements(self):
		self.update_list_gui()
		self.update_log_gui()
		
	def update_list_gui(self):
		self.widget_macros_list.clear()
		for key in self.macro_manager.macro_list:
			self.widget_macros_list.addItem(key)
	
	def update_log_gui(self):
		self.widget_macro_text.setText(str(self.current_macro["data"]))
	
	# methods relating to output
	def start_timer(self):
		print("started")
		frequency = self.settings_manager.settings["runtime"]["run_frequency"]
		self.timer = threading.Timer(frequency, self.tick)
		self.timer.start()
	
	def stop_timer(self):
		print("stopped")
		self.timer.cancel()
		self.timer = None
		
	def tick(self):
		print("running")
		self.run_once()
		self.start_timer()
	
	# callback
	def keybind_callback(self, event, data):
		if event == "ui_action_invoke":
			method_to_call = getattr(self, data[0])
			assert(callable(method_to_call))
			method_to_call()

