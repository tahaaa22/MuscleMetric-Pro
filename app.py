import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from login import *
from signup import *
from StrengthUI import *
from mobility_asesement import *
import serial
from pyfirmata import Arduino, util

# Initialize Arduino board
board = Arduino('COM6')
# Define the analog pin where your sensor is connected
analog_pin = board.get_pin('a:1:i')
it = util.Iterator(board)
it.start()

def read_sensor():
    # Read sensor value
    sensor_value = analog_pin.read()
    if sensor_value is not None:
        scaled_value = int(sensor_value * 1023)
    # Schedule the function to run again after 100 milliseconds
    window.after(100, read_sensor)
    return scaled_value

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_layout = None
        self.setupUi("signup")

        # Open the serial port
        #self.serialInst = serial.Serial("COM4", 9600)

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
            self.current_layout.loginbutton.clicked.connect(lambda: self.switch_layout("login"))
        elif layout_name == "login":
             self.current_layout.loginbutton.clicked.connect(lambda: self.switch_layout("StrenghtUI"))
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

    # def read_serial(self):
    #     if self.serialInst.in_waiting:
    #         # Read a line from the serial port
    #         packet = self.serialInst.readline()
    #         # Treat the line as the value itself
    #         value = packet.decode('utf-8').strip()
    #         # Convert the value to an integer
    #         try:
    #             value_int = int(value)
    #             # Update your widget with the received value
    #             self.current_layout.progressBar.setValue(value_int)
    #         except ValueError:
    #             print("Invalid value received from Arduino:", value)

    # def closeEvent(self, event):
    #     # Close the serial port when the window is closed
    #     self.serialInst.close()
    #     event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # Example of switching layout after some time (3 seconds)
    #QTimer.singleShot(3000, lambda: window.switch_layout("login"))

    sys.exit(app.exec_())
