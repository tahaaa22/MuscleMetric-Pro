import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from login import *
from signup import *
from StrengthUI import *
from mobility_asesement import *
import serial
from pyfirmata import Arduino, util

# # Initialize Arduino board
# board = Arduino('COM6')

# # Define the analog pin where your sensor is connected
# analog_pin = board.get_pin('a:1:i')
# analog_pin = board.get_pin('a:0:i')
# it = util.Iterator(board)
# it.start()

def read_sensor():
    pass
    # # Read sensor value
    # sensor_value = analog_pin.read()
    # if sensor_value is not None:
    #     scaled_value = int(sensor_value * 1023)
    # return scaled_value

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_layout = None
        self.setupUi("signup")
        # Create a QTimer to read serial periodically
        self.timer = QTimer(self)
        #self.timer.timeout.connect(self.read_serial)
        self.timer.start(100)  # Adjust the interval (milliseconds) as needed

    def setupUi(self, layout_name):
        if layout_name == "signup":
            self.current_layout = SignUp()
        elif layout_name == "login":
            self.current_layout = LogIn()
        elif layout_name == "StrenghtUI":
            self.current_layout = Ui_Infopage()
        elif layout_name == "assesement":
            self.current_layout = assesement()

        self.current_layout.setupUi(self)
        if layout_name == "signup":
            self.current_layout.signup.clicked.connect(lambda: self.switch_layout("login"))
        elif layout_name == "login":
             self.current_layout.Login_button.clicked.connect(lambda: self.switch_layout("StrenghtUI"))
        elif layout_name == "assesement":
            self.current_layout.returnbutton.clicked.connect(lambda: self.switch_layout("StrenghtUI"))
        elif layout_name == "StrenghtUI":
            ma = read_sensor()
            self.current_layout.maximum_muscle_strength_label.setText(ma)
            self.current_layout.Movement_Region.toggled.connect(lambda: self.switch_layout("assesement"))
        

    def switch_layout(self, layout_name):
        # Clear existing layout
        self.current_layout = None
        self.centralWidget().deleteLater()  # Clear existing widgets
        # Setup new layout
        self.setupUi(layout_name)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
