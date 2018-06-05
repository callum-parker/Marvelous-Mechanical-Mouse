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
		self.motion_speed = .001
		self.motion_variance = .03
		self.click_speed = 0.1
		self.click_variance = .1
		self.monitoring_service = Mouse_monitoring_service()
		
		# UI elements
		self.logstring = tk.StringVar()
		self.log_box = tk.Listbox(self, listvariable = self.logstring, width=58)
		self.log_box.grid(column=0, row=0, columnspan=5)
		
		# settings
		#labels
		self.speed_label = tk.Label(self, text="speed (s)")
		self.speed_label.grid(row=1, column=1)
		
		self.variance_label = tk.Label(self, text="variance (s)")
		self.variance_label.grid(row=1, column=2)
		
		self.motion_label = tk.Label(self, text="motion")
		self.motion_label.grid(row=2, column=0)
		
		self.click_label = tk.Label(self, text="click")
		self.click_label.grid(row=3, column=0)
		
		#entry boxes
		self.motion_speed_textbox_text = tk.StringVar()
		self.motion_speed_textbox_text.set(str(self.motion_speed))
		self.motion_speed_textbox = tk.Entry(self, width=6, textvariable=self.motion_speed_textbox_text)
		self.motion_speed_textbox.grid(row=2, column=1)
		
		self.motion_variance_textbox_text = tk.StringVar()
		self.motion_variance_textbox_text.set(str(self.motion_variance))
		self.motion_variance_textbox = tk.Entry(self, width=6, textvariable=self.motion_variance_textbox_text)
		self.motion_variance_textbox.grid(row=2, column=2)
		
		self.click_speed_textbox_text = tk.StringVar()
		self.click_speed_textbox_text.set(str(self.click_speed))
		self.click_speed_textbox = tk.Entry(self, width=6, textvariable=self.click_speed_textbox_text)
		self.click_speed_textbox.grid(row=3, column=1)
		
		self.click_variance_textbox_text = tk.StringVar()
		self.click_variance_textbox_text.set(str(self.click_variance))
		self.click_variance_textbox = tk.Entry(self, width=6, textvariable=self.click_variance_textbox_text)
		self.click_variance_textbox.grid(row=3, column=2)
		
		# buttons
		self.start_button = tk.Button(self, text="start recording", command=self.start_recording)
		self.start_button.grid(column=0, row=4)
		
		self.stop_button = tk.Button(self, text="stop recording", command=self.stop_recording)
		self.stop_button.grid(column=1, row=4)
		
		self.clear_button = tk.Button(self, text="clear recording", command=self.clear_recording)
		self.clear_button.grid(column=2, row=4)
		
		self.run_button = tk.Button(self, text="run once", command=self.run_macro)
		self.run_button.grid(column=3, row=4)
		
		self.quit_button = tk.Button(self, text="quit", command=self.quit)
		self.quit_button.grid(column=4, row=4)
	
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
		self.update_motion_speed()
		self.update_motion_variance()
		self.update_click_speed()
		self.update_click_variance()
		
		mouse_controller_thread = Mouse_controller(self.log, self.motion_speed, self.motion_variance, self.click_speed, self.click_variance)
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
			if log[i][3] == True or log[i][3] == None: # only record one click action from the two records of it
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
	
	def update_motion_speed(self):
		self.motion_speed = float(self.motion_speed_textbox_text.get())
	
	def update_motion_variance(self):
		self.motion_variance = float(self.motion_variance_textbox_text.get())
	
	def update_click_speed(self):
		self.click_speed = float(self.click_speed_textbox_text.get())
	
	def update_click_variance(self):
		self.click_variance = float(self.click_variance_textbox_text.get())

if __name__ == "__main__":
	
	# start main loop execution, using keyboard monitoring to parse commands
	ui = application_interface()
	ui.run()