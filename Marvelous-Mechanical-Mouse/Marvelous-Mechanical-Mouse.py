import sys
from gui.main_window import Main_window
from PyQt5.QtWidgets import QApplication

# start the application
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Main_window()
	window.show()
	sys.exit(app.exec_())