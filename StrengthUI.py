import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Infopage(object):
        def __init__(self) -> None:
                pass
        
        
        
        def Enable_measurements(self, checked):
                self.musclebox.setEnabled(checked)
                self.databox.setEnabled(checked)
                
                
        def measurements(self, value):
                self.muscle_strength_value_label.setText(value)
                

        def chosenMuscle(self):
                current_image = self.muscle_choice_combobox.currentText()
                self.muscle_choice_combobox
                if current_image == "biceps":
                        image = QtGui.QPixmap("biceps.jpg")
                else:
                        image = QtGui.QPixmap("calfs.jpg")
                # Define the desired width and height for the image
                desired_width = 350
                desired_height = 1000
                # Resize the image with the desired aspect ratio
                scaled_image = image.scaled(desired_width, desired_height, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
                # Set the resized image as the pixmap of the label
                self.image_label.setPixmap(scaled_image)
    
        def setupUi(self, Infopage):
                Infopage.setObjectName("Infopage")
                Infopage.resize(681, 667)
                self.centralwidget = QtWidgets.QWidget(Infopage)
                palette = QtGui.QPalette()
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
                brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
                brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
                brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
                brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
                brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
                brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
                self.centralwidget.setPalette(palette)
                self.centralwidget.setStyleSheet("background-color: #1e1e2f;\n"
                "border: 1.2px solid #ffffff;\n"
                "border-style: outset;\n"
                "border-radius: 15px;\n"
                "color:#ffffff;\n"
                "")
                self.centralwidget.setObjectName("centralwidget")
                self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
                self.gridLayout_3.setObjectName("gridLayout_3")
                self.welcomebox = QtWidgets.QGroupBox(self.centralwidget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.welcomebox.sizePolicy().hasHeightForWidth())
                self.welcomebox.setSizePolicy(sizePolicy)
                self.welcomebox.setMinimumSize(QtCore.QSize(500, 131))
                self.welcomebox.setMaximumSize(QtCore.QSize(16777215, 200))
                self.welcomebox.setObjectName("welcomebox")
                self.gridLayout = QtWidgets.QGridLayout(self.welcomebox)
                self.gridLayout.setObjectName("gridLayout")
                self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_6.setObjectName("horizontalLayout_6")
                self.welcome_2 = QtWidgets.QGroupBox(self.welcomebox)
                self.welcome_2.setStyleSheet("border:none;")
                self.welcome_2.setObjectName("welcome_2")
                self.welcome = QtWidgets.QVBoxLayout(self.welcome_2)
                self.welcome.setObjectName("welcome")
                self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_4.setObjectName("horizontalLayout_4")
                self.welcome_label = QtWidgets.QLabel(self.welcome_2)
                self.welcome_label.setMaximumSize(QtCore.QSize(16777215, 50))
                font = QtGui.QFont()
                font.setPointSize(18)
                self.welcome_label.setFont(font)
                self.welcome_label.setStyleSheet("border:none;")
                self.welcome_label.setObjectName("welcome_label")
                self.horizontalLayout_4.addWidget(self.welcome_label)
                spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_4.addItem(spacerItem)
                self.welcome.addLayout(self.horizontalLayout_4)
                self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_5.setObjectName("horizontalLayout_5")
                spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_5.addItem(spacerItem1)
                self.welcome_name_label = QtWidgets.QLabel(self.welcome_2)
                self.welcome_name_label.setMaximumSize(QtCore.QSize(16777215, 50))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.welcome_name_label.setFont(font)
                self.welcome_name_label.setStyleSheet("border:none;")
                self.welcome_name_label.setObjectName("welcome_name_label")
                self.horizontalLayout_5.addWidget(self.welcome_name_label)
                self.welcome.addLayout(self.horizontalLayout_5)
                self.horizontalLayout_6.addWidget(self.welcome_2)
                self.DateGender = QtWidgets.QGroupBox(self.welcomebox)
                self.DateGender.setStyleSheet("border:none;")
                self.DateGender.setObjectName("DateGender")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.DateGender)
                self.verticalLayout.setObjectName("verticalLayout")
                self.date_label = QtWidgets.QLabel(self.DateGender)
                self.date_label.setMaximumSize(QtCore.QSize(16777215, 23))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.date_label.setFont(font)
                self.date_label.setStyleSheet("border:none;")
                self.date_label.setObjectName("date_label")
                self.verticalLayout.addWidget(self.date_label)
                self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.DateGender)
                font = QtGui.QFont()
                font.setPointSize(9)
                self.dateTimeEdit.setFont(font)
                self.dateTimeEdit.setObjectName("dateTimeEdit")
                self.verticalLayout.addWidget(self.dateTimeEdit)
                self.date_label_2 = QtWidgets.QLabel(self.DateGender)
                self.date_label_2.setMaximumSize(QtCore.QSize(16777215, 23))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.date_label_2.setFont(font)
                self.date_label_2.setStyleSheet("border:none;")
                self.date_label_2.setObjectName("date_label_2")
                self.verticalLayout.addWidget(self.date_label_2)
                self.gender_label = QtWidgets.QLabel(self.DateGender)
                self.gender_label.setMaximumSize(QtCore.QSize(16777215, 32))
                self.gender_label.setStyleSheet("border: 1.2px solid #ffffff;\n"
                "border-style: outset;\n"
                "border-radius: 15px;")
                self.gender_label.setFrameShape(QtWidgets.QFrame.Box)
                self.gender_label.setText("")
                self.gender_label.setObjectName("gender_label")
                self.verticalLayout.addWidget(self.gender_label)
                self.horizontalLayout_6.addWidget(self.DateGender)
                self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
                self.gridLayout_3.addWidget(self.welcomebox, 0, 0, 1, 1)
                self.PreferenceBox = QtWidgets.QGroupBox(self.centralwidget)
                self.PreferenceBox.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
                self.PreferenceBox.setObjectName("PreferenceBox")
                self.gridLayout_2 = QtWidgets.QGridLayout(self.PreferenceBox)
                self.gridLayout_2.setObjectName("gridLayout_2")
                spacerItem2 = QtWidgets.QSpacerItem(640, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
                self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_7.setObjectName("horizontalLayout_7")
                self.date_label_3 = QtWidgets.QLabel(self.PreferenceBox)
                self.date_label_3.setMaximumSize(QtCore.QSize(16777215, 23))
                font = QtGui.QFont()
                font.setFamily("MS Shell Dlg 2")
                font.setPointSize(10)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.date_label_3.setFont(font)
                self.date_label_3.setStyleSheet("border:none;")
                self.date_label_3.setObjectName("date_label_3")
                self.horizontalLayout_7.addWidget(self.date_label_3)
                spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_7.addItem(spacerItem3)
                self.gridLayout_2.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
                self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_8.setObjectName("horizontalLayout_8")
                self.Muscle_Strength = QtWidgets.QRadioButton(self.PreferenceBox)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.Muscle_Strength.sizePolicy().hasHeightForWidth())
                self.Muscle_Strength.setSizePolicy(sizePolicy)
                self.Muscle_Strength.setMaximumSize(QtCore.QSize(16777215, 50))
                font = QtGui.QFont()
                font.setFamily("MS Shell Dlg 2")
                font.setPointSize(10)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.Muscle_Strength.setFont(font)
                self.Muscle_Strength.setStyleSheet("border: none;\n"
                                                "border-style: outset;\n"
                                                "border-radius: 15px;")
                self.Muscle_Strength.setObjectName("Muscle_Strength")
                self.horizontalLayout_8.addWidget(self.Muscle_Strength)
                self.Movement_Region = QtWidgets.QRadioButton(self.PreferenceBox)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.Movement_Region.sizePolicy().hasHeightForWidth())
                self.Movement_Region.setSizePolicy(sizePolicy)
                self.Movement_Region.setMaximumSize(QtCore.QSize(16777215, 50))
                font = QtGui.QFont()
                font.setFamily("MS Shell Dlg 2")
                font.setPointSize(10)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.Movement_Region.setFont(font)
                self.Movement_Region.setStyleSheet("border: none;\n"
                                                "border-style: outset;\n"
                                                "border-radius: 15px;")
                self.Movement_Region.setObjectName("Muscle_Strength")
                self.horizontalLayout_8.addWidget(self.Movement_Region)
                self.gridLayout_2.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)
                self.gridLayout_3.addWidget(self.PreferenceBox, 1, 0, 1, 1)
                self.musclebox = QtWidgets.QGroupBox(self.centralwidget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.musclebox.sizePolicy().hasHeightForWidth())
                self.musclebox.setSizePolicy(sizePolicy)
                self.musclebox.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.musclebox.setStyleSheet("border:none;")
                self.musclebox.setObjectName("musclebox")
                self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.musclebox)
                self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
                self.horizontalLayout_3.setObjectName("horizontalLayout_3")
                self.muscle_choice_layout = QtWidgets.QVBoxLayout()
                self.muscle_choice_layout.setObjectName("muscle_choice_layout")
                self.choose_muscle_label = QtWidgets.QLabel(self.musclebox)
                palette = QtGui.QPalette()
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
                brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
                brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
                brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
                brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
                brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
                brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
                brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
                brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
                brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
                brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
                brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
                brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
                self.choose_muscle_label.setPalette(palette)
                font = QtGui.QFont()
                font.setPointSize(11)
                self.choose_muscle_label.setFont(font)
                self.choose_muscle_label.setStyleSheet("border:none;")
                self.choose_muscle_label.setObjectName("choose_muscle_label")
                self.muscle_choice_layout.addWidget(self.choose_muscle_label)
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.muscle_choice_combobox = QtWidgets.QComboBox(self.musclebox)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.muscle_choice_combobox.setFont(font)
                self.muscle_choice_combobox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                "color: rgb(40,40,40);")
                self.muscle_choice_combobox.setObjectName("muscle_choice_combobox")
                self.muscle_choice_combobox.addItem("")
                self.muscle_choice_combobox.addItem("")
                self.horizontalLayout_2.addWidget(self.muscle_choice_combobox)
                self.muscle_choice_layout.addLayout(self.horizontalLayout_2)
                self.horizontalLayout_3.addLayout(self.muscle_choice_layout)
                spacerItem4 = QtWidgets.QSpacerItem(384, 17, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_3.addItem(spacerItem4)
                self.gridLayout_3.addWidget(self.musclebox, 2, 0, 1, 1)
                self.databox = QtWidgets.QGroupBox(self.centralwidget)
                self.databox.setStyleSheet("border:none;")
                self.databox.setObjectName("databox")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.databox)
                self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.all_muscle_info_layout = QtWidgets.QVBoxLayout()
                self.all_muscle_info_layout.setObjectName("all_muscle_info_layout")
                self.muscle_strength_info_layout = QtWidgets.QVBoxLayout()
                self.muscle_strength_info_layout.setObjectName("muscle_strength_info_layout")
                self.muscle_strength_label = QtWidgets.QLabel(self.databox)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.muscle_strength_label.setFont(font)
                self.muscle_strength_label.setStyleSheet("border:none;")
                self.muscle_strength_label.setObjectName("muscle_strength_label")
                self.muscle_strength_info_layout.addWidget(self.muscle_strength_label)
                self.muscle_strength_value_label = QtWidgets.QLabel(self.databox)
                self.muscle_strength_value_label.setStyleSheet("border: 1.2px solid #ffffff;\n"
                "border-style: outset;\n"
                "border-radius: 15px;")
                self.muscle_strength_value_label.setFrameShape(QtWidgets.QFrame.Box)
                self.muscle_strength_value_label.setText("")
                self.muscle_strength_value_label.setObjectName("muscle_strength_value_label")
                self.muscle_strength_info_layout.addWidget(self.muscle_strength_value_label)
                self.all_muscle_info_layout.addLayout(self.muscle_strength_info_layout)
                self.maximum_muscle_strength_info_layout = QtWidgets.QVBoxLayout()
                self.maximum_muscle_strength_info_layout.setObjectName("maximum_muscle_strength_info_layout")
                self.maximum_muscle_strength_label = QtWidgets.QLabel(self.databox)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.maximum_muscle_strength_label.setFont(font)
                self.maximum_muscle_strength_label.setStyleSheet("border:none;")
                self.maximum_muscle_strength_label.setObjectName("maximum_muscle_strength_label")
                self.maximum_muscle_strength_info_layout.addWidget(self.maximum_muscle_strength_label)
                self.maximum_muscle_strength_value_label = QtWidgets.QLabel(self.databox)
                self.maximum_muscle_strength_value_label.setStyleSheet("border: 1.2px solid #ffffff;\n"
                "border-style: outset;\n"
                "border-radius: 15px;")
                self.maximum_muscle_strength_value_label.setFrameShape(QtWidgets.QFrame.Box)
                self.maximum_muscle_strength_value_label.setText("")
                self.maximum_muscle_strength_value_label.setObjectName("maximum_muscle_strength_value_label")
                self.maximum_muscle_strength_info_layout.addWidget(self.maximum_muscle_strength_value_label)
                self.all_muscle_info_layout.addLayout(self.maximum_muscle_strength_info_layout)
                self.previous_muscle_strength_info_layout = QtWidgets.QVBoxLayout()
                self.previous_muscle_strength_info_layout.setObjectName("previous_muscle_strength_info_layout")
                self.previous_muscle_strength_label = QtWidgets.QLabel(self.databox)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.previous_muscle_strength_label.setFont(font)
                self.previous_muscle_strength_label.setStyleSheet("border:none;")
                self.previous_muscle_strength_label.setObjectName("previous_muscle_strength_label")
                self.previous_muscle_strength_info_layout.addWidget(self.previous_muscle_strength_label)
                self.previous_muscle_strength_value_label = QtWidgets.QLabel(self.databox)
                self.previous_muscle_strength_value_label.setStyleSheet("border: 1.2px solid #ffffff;\n"
                "border-style: outset;\n"
                "border-radius: 15px;")
                self.previous_muscle_strength_value_label.setFrameShape(QtWidgets.QFrame.Box)
                self.previous_muscle_strength_value_label.setText("")
                self.previous_muscle_strength_value_label.setObjectName("previous_muscle_strength_value_label")
                self.previous_muscle_strength_info_layout.addWidget(self.previous_muscle_strength_value_label)
                self.all_muscle_info_layout.addLayout(self.previous_muscle_strength_info_layout)
                self.horizontalLayout.addLayout(self.all_muscle_info_layout)
                spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout.addItem(spacerItem5)
                self.image_label = QtWidgets.QLabel(self.databox)
                self.image_label.setStyleSheet("border: none;\n"
                "border-style: outset;\n"
                "border-radius: 15px;")
                self.image_label.setFrameShape(QtWidgets.QFrame.Box)
                self.image_label.setLineWidth(1)
                self.image_label.setText("")
                
                image = QtGui.QPixmap("biceps.jpg")

                # Define the desired width and height for the image
                desired_width = 300
                desired_height = 800

                # Resize the image with the desired aspect ratio
                scaled_image = image.scaled(desired_width, desired_height, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
                # Set the resized image as the pixmap of the label
                self.image_label.setPixmap(scaled_image)
                self.image_label.setAlignment(QtCore.Qt.AlignCenter)
                self.image_label.setObjectName("image_label")
                self.horizontalLayout.addWidget(self.image_label)
                self.gridLayout_3.addWidget(self.databox, 3, 0, 1, 1)
                Infopage.setCentralWidget(self.centralwidget)

                self.retranslateUi(Infopage)
                QtCore.QMetaObject.connectSlotsByName(Infopage)
                self.musclebox.setEnabled(False)  
                self.databox.setEnabled(False)
                self.Muscle_Strength.toggled.connect(self.Enable_measurements)

        def retranslateUi(self, Infopage):
                _translate = QtCore.QCoreApplication.translate
                Infopage.setWindowTitle(_translate("Infopage", "MainWindow"))
                self.welcome_label.setText(_translate("Infopage", "Welcome"))
                self.welcome_name_label.setText(_translate("Infopage", "maryam!"))
                self.date_label.setText(_translate("Infopage", "Date:"))
                self.date_label_2.setText(_translate("Infopage", "Gender:"))
                self.PreferenceBox.setTitle(_translate("Infopage", "Preferences"))
                self.date_label_3.setText(_translate("Infopage", "Choose Your Current Measurments:"))
                self.Muscle_Strength.setText(_translate("Infopage", "Muscles Strength"))
                self.Movement_Region.setText(_translate("Infopage", "Movement Ragion"))
                self.choose_muscle_label.setText(_translate("Infopage", "Choose a muscle:"))
                self.muscle_choice_combobox.setItemText(0, _translate("Infopage", "biceps"))
                self.muscle_choice_combobox.setItemText(1, _translate("Infopage", "Calf"))
                self.muscle_strength_label.setText(_translate("Infopage", "Muscle Strength:"))
                self.maximum_muscle_strength_label.setText(_translate("Infopage", "Maximum Muscle Strength:"))
                self.previous_muscle_strength_label.setText(_translate("Infopage", "Previous Muscle Strength:"))


if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Infopage = QtWidgets.QMainWindow()
        ui = Ui_Infopage()
        ui.setupUi(Infopage)
        ui.chosenMuscle()
        ui.muscle_choice_combobox.currentIndexChanged.connect(ui.chosenMuscle)
        Infopage.show()
        sys.exit(app.exec_())
