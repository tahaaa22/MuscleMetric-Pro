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
 # Open the serial port
serialInst = serial.Serial("COM4", 9600)
def timer_timeout():
    print("Timer timeout occurred")
    

# timer = QTimer()
# timer.timeout.connect(timer_timeout)
# timer.setInterval(100)
# timer.start()
print("Timer started")  # Debug print to verify if the timer starts
#timer.timeout()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_layout = None
        self.setupUi("signup")
        self.sensor= 0
       

        # Create a QTimer to read serial periodically
        

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
            if timer.isActive():
                print("timer is still active")
            self.current_layout.returnbutton.clicked.connect(lambda: self.switch_layout("StrenghtUI"))
            self.current_layout.abduction_radioButton.clicked.connect(self.read_serial)
            self.current_layout.extension_radioButton.clicked.connect(self.read_serial)
            self.current_layout.flexion_radioButton.clicked.connect(self.read_serial)
            self.read_serial()  
        elif layout_name == "StrenghtUI":
            #self.current_layout.measurements(self.sensor)
            self.current_layout.Movement_Region.toggled.connect(lambda: self.switch_layout("assesement"))
    def read_serial(self):
        if serialInst.in_waiting >= 2:  # Check if at least two lines are available
            # Read two lines from the serial port
            #self.sensor = serialInst.readline().decode('utf-8').strip()
            lab = serialInst.readline().decode('utf-8').strip()
            degree = serialInst.readline().decode('utf-8').strip()
            precent = serialInst.readline().decode('utf-8').strip()

            # Treat the lines as the values themselves
            # Update your widgets with the received values
            if lab =='Abduction' :
                self.current_layout.abduction_deg_label.setText(degree)
                self.current_layout.abduction_progressBar.setValue(int(float(precent)))
            elif lab == 'Flexion':
                self.current_layout.flexio_deg_label.setText(degree)
                self.current_layout.flexion_progressBar.setValue(int(float(precent)))
            elif lab=='Hyperextension':
                self.current_layout.extension_deg_label.setText(degree)
                self.current_layout.extension_progressBar.setValue(int(float(precent)))
                # Example of updating another widget with the second value
                # self.anotherWidget.setValue(value_int2)    

    def switch_layout(self, layout_name):
        # Clear existing layout
        self.current_layout = None
        self.centralWidget().deleteLater()  # Clear existing widgets
        # Setup new layout
        if timer.isActive():
                print("timer is ACTIVve while switching")
        self.setupUi(layout_name)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(lambda: print("Event loop about to exit"))
    window = MainWindow()
    timer = QTimer()
    timer.timeout.connect(window.read_serial)
    timer.setInterval(1)
    timer.start()
    
    window.show()
    sys.exit(app.exec_())
