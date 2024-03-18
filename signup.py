import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QVBoxLayout

class SignUp(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(831, 466)
        Form.setSizeIncrement(QtCore.QSize(450, 550))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 831, 455))
        self.label.setStyleSheet("border-radius: 20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        
        # Load and set the image
        pixmap = QPixmap(r"signup-image.jpeg") 
        self.label.setPixmap(pixmap)
        
        # Set up the layout
        layout = QVBoxLayout(self.widget)
        layout.addWidget(self.label)
        self.widget.setLayout(layout)
        
        # Add the widget to the main layout
        self.gridLayout.addWidget(self.widget)
        self.ACCOUNT = QtWidgets.QGroupBox(self.widget)
        self.ACCOUNT.setGeometry(QtCore.QRect(0, 20, 321, 81))
        self.ACCOUNT.setStyleSheet("border:none;\n"
"")
        self.ACCOUNT.setObjectName("ACCOUNT")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.ACCOUNT)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(168, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.createanaccount = QtWidgets.QLabel(self.ACCOUNT)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(30)
        font.setItalic(False)
        self.createanaccount.setFont(font)
        self.createanaccount.setStyleSheet("font: 300 24pt \"Bahnschrift Light SemiCondensed\";\n"
"color: rgb(9, 9, 9);")
        self.createanaccount.setObjectName("createanaccount")
        self.horizontalLayout.addWidget(self.createanaccount)
        spacerItem1 = QtWidgets.QSpacerItem(168, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.ACCOUNT)
        self.label_3.setStyleSheet("color: rgb(115, 115, 115);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.login = QtWidgets.QPushButton(self.ACCOUNT)
        self.login.setStyleSheet("border:none;\n"
"color: rgb(62, 97, 255)")
        self.login.setObjectName("login")
        self.horizontalLayout_5.addWidget(self.login)
        spacerItem2 = QtWidgets.QSpacerItem(118, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.MAILANDPASS = QtWidgets.QGroupBox(self.widget)
        self.MAILANDPASS.setGeometry(QtCore.QRect(20, 110, 301, 241))
        self.MAILANDPASS.setStyleSheet("border:none;")
        self.MAILANDPASS.setObjectName("MAILANDPASS")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.MAILANDPASS)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.MAILANDPASS)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.MAIL = QtWidgets.QGroupBox(self.MAILANDPASS)
        self.MAIL.setStyleSheet("border:none;")
        self.MAIL.setObjectName("MAIL")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.MAIL)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.enteremail = QtWidgets.QTextEdit(self.MAIL)
        self.enteremail.setStyleSheet("background-color: rgba(0 ,0 ,0 ,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(9,9,9);\n"
"padding-bottom:7px;\n"
"color: rgb(9, 9, 9);\n"
"")
        self.enteremail.setObjectName("enteremail")
        self.horizontalLayout_2.addWidget(self.enteremail)
        spacerItem3 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2.addWidget(self.MAIL)
        self.label_6 = QtWidgets.QLabel(self.MAILANDPASS)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.PASSWORD1 = QtWidgets.QGroupBox(self.MAILANDPASS)
        self.PASSWORD1.setObjectName("PASSWORD1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.PASSWORD1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.PASSWORD1 = QtWidgets.QTextEdit(self.PASSWORD1)
        font = QtGui.QFont()
        font.setFamily("Simple Bold Jut Out")
        self.PASSWORD1.setFont(font)
        self.PASSWORD1.setStyleSheet("background-color: rgba(0 ,0 ,0 ,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(9,9,9, 255);\n"
"color: rgb(9, 9, 9);\n"
"padding-bottom:7px;\n"
"")
        self.PASSWORD1.setObjectName("PASSWORD1")
        self.horizontalLayout_3.addWidget(self.PASSWORD1)
        spacerItem4 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_2.addWidget(self.PASSWORD1)
        self.CONFPASS = QtWidgets.QGroupBox(self.MAILANDPASS)
        self.CONFPASS.setObjectName("CONFPASS")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.CONFPASS)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.confirmpass = QtWidgets.QTextEdit(self.CONFPASS)
        font = QtGui.QFont()
        font.setFamily("Simple Bold Jut Out")
        self.confirmpass.setFont(font)
        self.confirmpass.setStyleSheet("background-color: rgba(0 ,0 ,0 ,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(9,9,9, 255);\n"
"color: rgb(9, 9, 9);\n"
"padding-bottom:7px;\n"
"")
        self.confirmpass.setObjectName("confirmpass")
        self.horizontalLayout_4.addWidget(self.confirmpass)
        spacerItem5 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout_2.addWidget(self.CONFPASS)
        self.layoutWidget = QtWidgets.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 350, 301, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.signuobox = QtWidgets.QGroupBox(self.layoutWidget)
        self.signuobox.setMaximumSize(QtCore.QSize(16777215, 55))
        self.signuobox.setStyleSheet("border:none;\n"
"")
        self.signuobox.setObjectName("signuobox")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.signuobox)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.signup = QtWidgets.QPushButton(self.signuobox)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(16)
        font.setItalic(False)
        self.signup.setFont(font)
        self.signup.setStyleSheet("font: 300 16pt \"Bahnschrift Light SemiCondensed\";\n"
"background-color: rgb(62, 97, 255);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.signup.setObjectName("signup")
        self.horizontalLayout_6.addWidget(self.signup)
        spacerItem6 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.verticalLayout_3.addWidget(self.signuobox)
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox.setStyleSheet("Font: 7pt;color: rgb(115, 115, 115);")
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_3.addWidget(self.checkBox)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.createanaccount.setText(_translate("Form", "Create An Account"))
        self.label_3.setText(_translate("Form", "Already Have An Acount?"))
        self.login.setText(_translate("Form", "Log in"))
        self.label_5.setText(_translate("Form", "Email address"))
        self.enteremail.setPlaceholderText(_translate("Form", "Enter Email"))
        self.label_6.setText(_translate("Form", "PassWord"))
        self.PASSWORD1.setPlaceholderText(_translate("Form", "PassWord"))
        self.confirmpass.setPlaceholderText(_translate("Form", "Confirm Password"))
        self.signup.setText(_translate("Form", "sign Up"))
        self.checkBox.setText(_translate("Form", "I agree to the Terms of service and privacy policy"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = SignUp()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
