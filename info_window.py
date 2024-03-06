import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Infopage(object):
    def setupUi(self, Infopage):
        Infopage.setObjectName("Infopage")
        Infopage.resize(648, 467)
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
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.welcomebox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welcomebox.sizePolicy().hasHeightForWidth())
        self.welcomebox.setSizePolicy(sizePolicy)
        self.welcomebox.setMinimumSize(QtCore.QSize(500, 131))
        self.welcomebox.setMaximumSize(QtCore.QSize(16777215, 200))
        self.welcomebox.setObjectName("welcomebox")
        self.welcome_horizontalLayout = QtWidgets.QHBoxLayout(self.welcomebox)
        self.welcome_horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.welcome_horizontalLayout.setSpacing(7)
        self.welcome_horizontalLayout.setObjectName("welcome_horizontalLayout")
        self.welcome_label = QtWidgets.QLabel(self.welcomebox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.welcome_label.setFont(font)
        self.welcome_label.setStyleSheet("border:none;")
        self.welcome_label.setObjectName("welcome_label")
        self.welcome_horizontalLayout.addWidget(self.welcome_label)
        self.welcome_name_label = QtWidgets.QLabel(self.welcomebox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.welcome_name_label.setFont(font)
        self.welcome_name_label.setStyleSheet("border:none;")
        self.welcome_name_label.setObjectName("welcome_name_label")
        self.welcome_horizontalLayout.addWidget(self.welcome_name_label)
        self.date_verticalLayout = QtWidgets.QVBoxLayout()
        self.date_verticalLayout.setObjectName("date_verticalLayout")
        self.date_label = QtWidgets.QLabel(self.welcomebox)
        self.date_label.setStyleSheet("border:none;")
        self.date_label.setObjectName("date_label")
        self.date_verticalLayout.addWidget(self.date_label)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.welcomebox)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.date_verticalLayout.addWidget(self.dateTimeEdit)
        self.welcome_horizontalLayout.addLayout(self.date_verticalLayout)
        self.verticalLayout.addWidget(self.welcomebox)
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
        self.choose_muscle_label.setStyleSheet("border:none;")
        self.choose_muscle_label.setObjectName("choose_muscle_label")
        self.muscle_choice_layout.addWidget(self.choose_muscle_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.muscle_choice_combobox = QtWidgets.QComboBox(self.musclebox)
        self.muscle_choice_combobox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(40,40,40);")
        self.muscle_choice_combobox.setObjectName("muscle_choice_combobox")
        self.muscle_choice_combobox.addItem("")
        self.muscle_choice_combobox.addItem("")
        self.horizontalLayout_2.addWidget(self.muscle_choice_combobox)
        self.muscle_choice_layout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.muscle_choice_layout)
        spacerItem = QtWidgets.QSpacerItem(384, 17, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addWidget(self.musclebox)
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
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.image_label = QtWidgets.QLabel(self.databox)
        self.image_label.setStyleSheet("border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;")
        self.image_label.setFrameShape(QtWidgets.QFrame.Box)
        self.image_label.setLineWidth(1)
        self.image_label.setText("")
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setObjectName("image_label")
        self.horizontalLayout.addWidget(self.image_label)
        self.verticalLayout.addWidget(self.databox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        Infopage.setCentralWidget(self.centralwidget)

        self.retranslateUi(Infopage)
        QtCore.QMetaObject.connectSlotsByName(Infopage)

    def retranslateUi(self, Infopage):
        _translate = QtCore.QCoreApplication.translate
        Infopage.setWindowTitle(_translate("Infopage", "MainWindow"))
        self.welcome_label.setText(_translate("Infopage", "Welcome"))
        self.welcome_name_label.setText(_translate("Infopage", "maryam!                                               "))
        self.date_label.setText(_translate("Infopage", "Date:"))
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
    Infopage.show()
    sys.exit(app.exec_())
