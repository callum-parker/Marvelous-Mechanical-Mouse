from mouse_monitoring_service import Mouse_monitoring_service
from mouse_controller import Mouse_controller

import threading
import tkinter as tk

class application_interface:
	application_name = "Marvelous Mechanical Mouse"
		
	def run(self):
		root = tk.Tk()
		
		main_window = Main_window(root)
		main_window.master.title(self.application_name)
		main_window.pack()
		root.mainloop()
		exit()

class Main_window (tk.Frame):

	def __init__(self, parent):
		tk.Frame.__init__(self, parent)
		
		# data
		self.log = []
		self.monitoring_service = Mouse_monitoring_service()
		
		# UI elements
		self.logstring = tk.StringVar()
		self.log_box = tk.Listbox(self, listvariable = self.logstring, width=58)
		self.log_box.grid(column=0, row=0, columnspan=5)
		
		self.start_button = tk.Button(self, text="start recording", command=self.start_recording)
		self.start_button.grid(column=0, row=1)
		
		self.stop_button = tk.Button(self, text="stop recording", command=self.stop_recording)
		self.stop_button.grid(column=1, row=1)
		
		self.clear_button = tk.Button(self, text="clear recording", command=self.clear_recording)
		self.clear_button.grid(column=2, row=1)
		
		self.run_button = tk.Button(self, text="run once", command=self.run_macro)
		self.run_button.grid(column=3, row=1)
		
		self.quit_button = tk.Button(self, text="quit", command=self.quit)
		self.quit_button.grid(column=4, row=1)
	
	def start_recording(self):
		self.monitoring_service = Mouse_monitoring_service()
		self.monitoring_service.start()
		
	def stop_recording(self):
		self.monitoring_service.stop()
		self.update_log()
		self.update_log_gui()
	
	def clear_recording(self):
		self.monitoring_service.clear_log()
		self.clear_log()
		self.update_log_gui()
	
	def run_macro(self):
		mouse_controller_thread = Mouse_controller(self.log)
		mouse_controller_thread.start()
		mouse_controller_thread.join()
		
	def quit(self):
		exit()
	
	def run(self):
		self.pack()
		self.mainloop()
		
	# utility functions
	def parse_log(self, log):
		action_list = []
		for i in range(0, len(log)-2):
			if log[i][3] == True: # only record one click action from the two records of it
				new_record = {}
				new_record["x"] = log[i][0]
				new_record["y"] = log[i][1]
				new_record["action"] = log[i][2]
				
				action_list.append(new_record)
		return action_list
	
	def update_log(self):
		self.log += self.parse_log(self.monitoring_service.log)
	
	def clear_log(self):
		self.log = []
	
	def update_log_gui(self):
		self.logstring.set(self.log)

if __name__ == "__main__":
	# start main loop execution, using keyboard monitoring to parse commands
	ui = application_interface()
	ui.run()