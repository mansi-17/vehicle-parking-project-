from PyQt5.QtWidgets import QWidget,QVBoxLayout,QPushButton,QLabel,QLineEdit,QFrame,QHBoxLayout
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import QRegExp
from DataBaseOperation import DBOperation
import json
import re

global reg1, reg2, reg3, reg4


class registerscreen(QWidget):
   def __init__(self):
        super(registerscreen,self).__init__()
        self.setWindowTitle("User register")
        self.resize(300,300)
        layout = QVBoxLayout()
        label_user_username = QLabel("Username")
        label_user_username.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")
        label_user_password = QLabel("Password")
        label_user_password.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")
        label_phone = QLabel("PHONE NUMBER")
        label_phone.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")
        label_Email = QLabel("EMAIL")
        label_Email.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")

        self.input_user_username = QLineEdit(self)
        reg1 = QRegExp("^[A-Za-z]{10}$")
        input_1 = QRegExpValidator(reg1,self.input_user_username)
        self.input_user_username.setMaxLength(10)
        self.input_user_username.setValidator(input_1)
        self.input_user_username.setStyleSheet("padding:5px;font-size:17px")
        self.input_user_password = QLineEdit(self)
        reg2 = QRegExp("^[A-Za-z0-9]{15}")
        input_2 = QRegExpValidator(reg2, self.input_user_password)
        self.input_user_password.setValidator(input_2)
        self.input_user_password.setStyleSheet("padding:5px;font-size:17px")
        self.input_user_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_phone = QLineEdit()
        self.input_phone.setValidator(QIntValidator())
        reg3 = QRegExp("[0-9]{10}")
        self.input_phone.setMaxLength(10)
        input_3 = QRegExpValidator(reg3, self.input_phone)

        self.input_phone.setValidator(input_3)
        self.input_phone.setStyleSheet("padding:5px;font-size:17px")
        self.input_email = QLineEdit()
        self.input_email.setStyleSheet("padding:5px;font-size:17px")

        btn_regis = QPushButton("Register")
        btn_regis.setStyleSheet("padding:7px;font-size:20px;background:green;color:#fff")
        self.error_label = QLabel()
        self.error_label.setStyleSheet("color:red;padding:8px 0px;font-size:18px;text-align:center;")

        layout.addWidget(label_user_username)
        layout.addWidget(self.input_user_username)
        layout.addWidget(label_user_password)
        layout.addWidget(self.input_user_password)
        layout.addWidget(label_phone)
        layout.addWidget(self.input_phone)
        layout.addWidget(label_Email)
        layout.addWidget(self.input_email)
        layout.addWidget(btn_regis)
        layout.addWidget(self.error_label)

        btn_regis.clicked.connect(self.showStepInfo)

        self.setLayout(layout)



   def showStepInfo(self):
       if self.input_user_username.text() == "":
           self.error_label.setText("Enter correct input for USERNAME")
           return

       if self.input_user_password.text() == "":
           self.error_label.setText("Enter correct input for PASSWORD")
           return

       if len(self.input_user_password.text()) <= 7:
           self.error_label.setText("Password lenght should be more than 7")
           return

       if self.input_phone.text() == "":
           self.error_label.setText("Enter correct input for PHONE NUMBER")
           return
       if len(self.input_phone.text()) != 10:
           self.error_label.setText("Number Not valid")
           return

       if self.input_email.text() == "":
           self.error_label.setText("Enter correct input for EMAIL ID")
           return
       if (self.input_email.text().endswith("@gmail.com")) == False:
           self.error_label.setText("Enter correct input for EMAIL ID")
           return
       counter = self.input_email.text().count("@gmail.com")
       if counter > 1:
           self.error_label.setText("Enter correct input for EMAIL ID")
           return
       counter1 = self.input_email.text().count("@")
       counter2 = self.input_email.text().count(".com")
       if counter1 > 1:
           self.error_label.setText("Enter correct input for EMAIL ID")
           return
       if counter2 > 1:
           self.error_label.setText("Enter correct input for EMAIL ID")
           return




       dboperation = DBOperation()
       dboperation.InsertAdmin(self.input_user_username.text(), self.input_user_password.text(),self.input_phone.text(), self.input_email.text())
       print("save data")
       self.close()
