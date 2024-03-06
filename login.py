from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from info_window import *
import sqlite3
from hashlib import sha256
 # Connect to the SQLite database (will create it if it doesn't exist)
conn = sqlite3.connect('user_credentials.db')

        # Create a cursor object to execute SQL queries
cursor = conn.cursor()
class Ui_MainWindow(object):
        def __init__(self) :
                self.Ui_Infopage = Ui_Infopage()
                self.newwindow = QtWidgets.QMainWindow()
                self.Ui_Infopage.setupUi(self.newwindow)
                self.Ui_Infopage.muscle_choice_combobox.currentIndexChanged.connect(self.Ui_Infopage.chosenMuscle)
                # Create a table to store usernames, hashed passwords, and measurements
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS me (
                        id INTEGER PRIMARY KEY,
                        username TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL,
                        measurement INTEGER
                )
                ''')

        # Function to get the maximum measurement for a given username
        def get_max(self,username):
                cursor.execute('SELECT measurement FROM me WHERE username = ?', (username,))
                result = cursor.fetchone()
                return result[0] if result else 0
        # Function to hash a password
        def hash_password(self, password):
                return sha256(password.encode()).hexdigest()

        def add_user(self,username, password, measurement):
                hashed_password = self.hash_password(password)
                cursor.execute('INSERT INTO me (username, password, measurement) VALUES (?, ?, ?)', (username, hashed_password, measurement))
                conn.commit()
                print("User added successfully!")
                
                     
        def start_app(self, main):
                name = self.username.text()
                password = self.password.text()
                self.Ui_Infopage.welcome_name_label.setText(name)
                max = self.Ui_Infopage.maximum_muscle_strength_value_label.text()
                #self.add_user(name,password, max)
                if self.password.text() != "":
                        self.newwindow.show()
                        new_max = self.get_max(name)
                        self.Ui_Infopage.previous_muscle_strength_value_label.setText(str(new_max))
                        #main.close()
                     

        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(587, 622)
                MainWindow.setStyleSheet("background-color: #1e1e2f;\n"
        "border: 1.2px solid #ffffff;")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
                self.gridLayout.setObjectName("gridLayout")
                self.labelbox = QtWidgets.QGroupBox(self.centralwidget)
                self.labelbox.setStyleSheet("border:none;")
                self.labelbox.setObjectName("labelbox")
                self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.labelbox)
                self.horizontalLayout_3.setObjectName("horizontalLayout_3")
                spacerItem = QtWidgets.QSpacerItem(88, 9, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_3.addItem(spacerItem)
                self.label = QtWidgets.QLabel(self.labelbox)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
                self.label.setSizePolicy(sizePolicy)
                self.label.setMaximumSize(QtCore.QSize(16777215, 100))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(48)
                font.setBold(True)
                font.setWeight(75)
                self.label.setFont(font)
                self.label.setToolTip("")
                self.label.setWhatsThis("")
                self.label.setStyleSheet("color: rgb(225, 225, 225);font-size:48pt;\n"
        "border:None;")
                self.label.setAlignment(QtCore.Qt.AlignCenter)
                self.label.setObjectName("label")
                self.horizontalLayout_3.addWidget(self.label)
                spacerItem1 = QtWidgets.QSpacerItem(118, 9, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_3.addItem(spacerItem1)
                self.gridLayout.addWidget(self.labelbox, 0, 0, 1, 1)
                spacerItem2 = QtWidgets.QSpacerItem(20, 68, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
                self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
                self.inputbox = QtWidgets.QGroupBox(self.centralwidget)
                self.inputbox.setStyleSheet("border:none;")
                self.inputbox.setObjectName("inputbox")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.inputbox)
                self.verticalLayout.setSpacing(34)
                self.verticalLayout.setObjectName("verticalLayout")
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_2.setSpacing(50)
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.label_3 = QtWidgets.QLabel(self.inputbox)
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(15)
                font.setBold(True)
                font.setWeight(75)
                self.label_3.setFont(font)
                self.label_3.setStyleSheet("font-size:15pt;\n"
        "color:rgb(142, 142, 213);\n"
        "border: None;")
                self.label_3.setObjectName("label_3")
                self.horizontalLayout_2.addWidget(self.label_3)
                self.username = QtWidgets.QLineEdit(self.inputbox)
                self.username.setStyleSheet("font-size:13pt; color:rgb(243,243,243);\n"
        "")
                self.username.setObjectName("username")
                self.horizontalLayout_2.addWidget(self.username)
                self.verticalLayout.addLayout(self.horizontalLayout_2)
                self.horizontalLayout = QtWidgets.QHBoxLayout()
                self.horizontalLayout.setSpacing(63)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.label_2 = QtWidgets.QLabel(self.inputbox)
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(15)
                font.setBold(True)
                font.setWeight(75)
                self.label_2.setFont(font)
                self.label_2.setStyleSheet("font-size:15pt;\n"
        "color:rgb(142, 142, 213);\n"
        "Border: None;")
                self.label_2.setObjectName("label_2")
                self.horizontalLayout.addWidget(self.label_2)
                self.password = QtWidgets.QLineEdit(self.inputbox)
                self.password.setStyleSheet("font-size:13pt; color:rgb(243,243,243);")
                self.password.setObjectName("password")
                self.horizontalLayout.addWidget(self.password)
                self.verticalLayout.addLayout(self.horizontalLayout)
                self.gridLayout.addWidget(self.inputbox, 2, 0, 1, 1)
                spacerItem3 = QtWidgets.QSpacerItem(20, 68, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
                self.gridLayout.addItem(spacerItem3, 3, 0, 1, 1)
                self.loginbox = QtWidgets.QGroupBox(self.centralwidget)
                self.loginbox.setStyleSheet("border:none;")
                self.loginbox.setObjectName("loginbox")
                self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.loginbox)
                self.horizontalLayout_4.setObjectName("horizontalLayout_4")
                spacerItem4 = QtWidgets.QSpacerItem(88, 9, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_4.addItem(spacerItem4)
                self.loginbutton = QtWidgets.QPushButton(self.loginbox)
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.loginbutton.setFont(font)
                self.loginbutton.setStyleSheet("color:rgb(142, 142, 213); \n"
        "border: 2px solid  rgb(142, 142, 213);\n"
        "border-style: outset;\n"
        "border-radius: 15px;")
                self.loginbutton.setObjectName("loginbutton")
                self.horizontalLayout_4.addWidget(self.loginbutton)
                spacerItem5 = QtWidgets.QSpacerItem(118, 14, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_4.addItem(spacerItem5)
                self.gridLayout.addWidget(self.loginbox, 4, 0, 1, 1)
                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.label.setText(_translate("MainWindow", "LogIn"))
                self.label_3.setText(_translate("MainWindow", "UserName:"))
                self.label_2.setText(_translate("MainWindow", "Password:"))
                self.loginbutton.setText(_translate("MainWindow", "LogIn"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.loginbutton.clicked.connect(lambda: ui.start_app(MainWindow))
    MainWindow.show()
    sys.exit(app.exec_())
