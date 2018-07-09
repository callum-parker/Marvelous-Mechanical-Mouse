import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QDialogButtonBox
from PyQt5 import QtGui 

from .dialogs.settings_window import Ui_Dialog as Settings_window_ui

from global_settings import Global_settings

class Settings_window (QDialog, Settings_window_ui):
	def __init__(self, settings_manager):
		super(Settings_window, self).__init__()
		
		# set class data and objects
		self.settings_manager = settings_manager
		
		# set up GUI
		self.setupUi(self)
		
		# special case for the apply button connect
		self.buttonBox.button(QDialogButtonBox.Apply).clicked.connect(self.apply)
		
		# set validators
		validator = QtGui.QDoubleValidator()
		self.widget_lineedit_movement_speed.setValidator(validator)
		self.widget_lineedit_movement_variance.setValidator(validator)
		self.widget_lineedit_click_speed.setValidator(validator)
		self.widget_lineedit_click_variance.setValidator(validator)
		self.widget_lineedit_run_frequency.setValidator(validator)
		
		# set the initial values
		self.update_fields()
		
	def accept(self):
		self.save()
		super(Settings_window, self).accept()
	
	def reject(self):
		super(Settings_window, self).reject()
	
	def apply(self):
		self.save()
	
	def save(self):
		# the settings data
		settings = self.settings_manager.settings
		
		# get the properties
		movement_speed = float(self.widget_lineedit_movement_speed.text())
		movement_variance = float(self.widget_lineedit_movement_variance.text())
		click_speed = float(self.widget_lineedit_click_speed.text())
		click_variance = float(self.widget_lineedit_click_variance.text())
		run_frequency = float(self.widget_lineedit_run_frequency.text())
		
		# set the appropriate records
		settings["mouse"]["movement_speed"] = movement_speed
		settings["mouse"]["movement_variance"] = movement_variance
		settings["mouse"]["click_speed"] = click_speed
		settings["mouse"]["click_variance"] = click_variance
		settings["runtime"]["run_frequency"] = run_frequency
		
		# save changes
		self.settings_manager.save()
		
	def update_fields(self):
		# the settings data
		settings = self.settings_manager.settings
		
		# get the properties
		movement_speed = str(settings["mouse"]["movement_speed"])
		movement_variance = str(settings["mouse"]["movement_variance"])
		click_speed = str(settings["mouse"]["click_speed"])
		click_variance = str(settings["mouse"]["click_variance"])
		run_frequency = str(settings["runtime"]["run_frequency"])
	
		# set the appropriate fields
		self.widget_lineedit_movement_speed.setText(movement_speed)
		self.widget_lineedit_movement_variance.setText(movement_variance)
		self.widget_lineedit_click_speed.setText(click_speed)
		self.widget_lineedit_click_variance.setText(click_variance)
		self.widget_lineedit_run_frequency.setText(run_frequency)


# start the application
if __name__ == "__main__":
	settings_save_file_location = "settings.ini"
	settings_manager = Global_settings(settings_save_file_location)
	app = QApplication(sys.argv)
	window = Settings_window(settings_manager)
	window.show()
	sys.exit(app.exec_())