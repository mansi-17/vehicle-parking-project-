from PyQt5.QtWidgets import QWidget,QPushButton,QVBoxLayout,QLabel,QLineEdit
from login import loginscreen
import json
from DataBaseOperation import DBOperation
from PyQt5 import QtWidgets,QtCore

class InstallWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User parking")
        self.resize(400,400)

        layout=QVBoxLayout()

        label_db_name=QLabel("database name")
        label_db_username = QLabel("database username")
        label_db_password = QLabel("database password")
        label_user_username = QLabel("Username")
        label_user_password = QLabel("Password")
        label_phone = QLabel("PHONE NUMBER")
        label_Email = QLabel("EMAIL")
        label_no_of_two_seater = QLabel("No of two wheeler vehicle")
        label_no_of_four_seater = QLabel("No of Four wheeler vehicle")

        self.input_db_name = QLineEdit()
        self.input_db_name.setText("userpak")
        self.input_db_username = QLineEdit()
        self.input_db_username.setText("user")
        self.input_db_password = QLineEdit()
        self.input_db_password.setText("password")
        self.input_user_username= QLineEdit()
        self.input_user_password = QLineEdit()
        self.input_user_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_phone = QLineEdit()
        self.input_email = QLineEdit()
        self.input_two_wheeler = QLineEdit()
        self.input_four_wheeler = QLineEdit()

        buttonsave = QPushButton("save data")
        self.error_label = QLabel()
        self.error_label.setStyleSheet("color:red")

        layout.addWidget(label_db_name)
        layout.addWidget(self.input_db_name)
        layout.addWidget(label_db_username)
        layout.addWidget(self.input_db_username)
        layout.addWidget(label_db_password)
        layout.addWidget(self.input_db_password)
        layout.addWidget(label_user_username)
        layout.addWidget(self.input_user_username)
        layout.addWidget(label_user_password)
        layout.addWidget(self.input_user_password)
        layout.addWidget(label_phone)
        layout.addWidget(self.input_phone)
        layout.addWidget(label_Email)
        layout.addWidget(self.input_email)
        layout.addWidget(label_no_of_two_seater)
        layout.addWidget(self.input_two_wheeler)
        layout.addWidget(label_no_of_four_seater)
        layout.addWidget(self.input_four_wheeler)
        layout.addWidget(buttonsave)
        layout.addWidget(self.error_label)

        buttonsave.clicked.connect(self.showStepInfo)

        self.setLayout(layout)

    def showStepInfo(self):
            if self.input_db_name.text() == "":
                self.error_label.setText("Enter correct input for DB NAME")
                return

            if self.input_db_username.text() == "":
                self.error_label.setText("Enter correct input for DB USERNAME")
                return

            if self.input_db_password.text() == "":
                self.error_label.setText("Enter correct input for DB PASSWORD")
                return

            if self.input_user_username.text() =="":
                self.error_label.setText("Enter correct input for USERNAME")
                return

            if self.input_user_password.text() == "":
                self.error_label.setText("Enter correct input for PASSWORD")
                return

            if self.input_phone.text() == "":
                self.error_label.setText("Enter correct input for PHONE NUMBER")
                return

            if self.input_email.text() == "":
                self.error_label.setText("Enter correct input for EMAIL ID")
                return
            if self.input_two_wheeler.text() == "":
                self.error_label.setText("Enter correct input for TWO WHEELER")
                return

            if self.input_four_wheeler.text() == "":
                self.error_label.setText("Enter correct input for FOUR WHEELER")
                return

            data = {"username": self.input_db_username.text(), "database": self.input_db_name.text(),"password": self.input_db_password.text()}
            file = open("./config.json", "w")
            file.write(json.dumps(data))
            file.close()
            dboperation = DBOperation()
            dboperation.Createtable()
            dboperation.InsertAdmin(self.input_user_username.text(),self.input_user_password.text(),self.input_phone.text(),self.input_email.text())
            dboperation.INSERTONETIMEDATA(int(self.input_two_wheeler.text()),int(self.input_four_wheeler.text()))

            self.close()
            self.login = loginscreen()
            self.login.showloginscreen()
            print("save data")


