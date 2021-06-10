from PyQt5.QtWidgets import QWidget,QVBoxLayout,QPushButton,QLabel,QLineEdit,QFrame,QHBoxLayout
from home import homescreen
from DataBaseOperation import DBOperation
from PyQt5 import QtWidgets,QtCore
from register import registerscreen

class loginscreen(QWidget):
    def __init__(self):
        super(loginscreen, self).__init__()
        self.setWindowTitle("User Login")
        self.resize(300,50)
        layout=QVBoxLayout()
        label_username=QLabel("username:")
        label_username.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")
        self.input_username=QLineEdit()
        self.input_username.setStyleSheet("padding:5px;font-size:17px")
        label_password=QLabel("password :")
        label_password.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password.setStyleSheet("padding:5px;font-size:17px")
        self.error_msg = QLabel()
        self.error_msg.setStyleSheet("color:red;padding:8px 0px;font-size:18px;text-align:center;")

        self.btn_login = QPushButton("Login")
        self.btn_login.setStyleSheet("padding:7px;font-size:20px;background:green;color:#fff")
        self.btn_register = QPushButton("Register")
        self.btn_register.setStyleSheet("padding:7px;font-size:20px;background:green;color:#fff")
        layout.addWidget(label_username)
        layout.addWidget(self.input_username)
        layout.addWidget(label_password)
        layout.addWidget(self.input_password)
        layout.addWidget(self.btn_login)
        layout.addWidget(self.btn_register)
        layout.addWidget(self.error_msg)
        layout.addStretch()


        self.btn_login.clicked.connect(self.showhome)
        self.btn_register.clicked.connect(self.registe)

        self.setLayout(layout)

    def showloginscreen(self):
        self.show()

    def showhome(self):
            if self.input_username.text() == "":
                self.error_msg.setText("Please enter username")
                return
            if self.input_password.text() == "":
                self.error_msg.setText("Please enter password")
                return
            dboperation = DBOperation()
            result = dboperation.doadminlogin(self.input_username.text(), self.input_password.text())
            if result:
                self.error_msg.setText("Login Successfully")
                self.close()
                self.home = homescreen()
                self.home.show()
            else:
                self.error_msg.setText("Invalid Login Please Try Again Later")

    def registe(self):
        self.register = registerscreen()
        self.register.show()












