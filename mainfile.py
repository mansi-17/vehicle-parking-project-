import sys
import os
from PyQt5.QtWidgets import QApplication,QSplashScreen,QLabel
from login import loginscreen
from installing import InstallWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt,QTimer

class MainScreen():
    def showsplashscreen(self):
        self.pix=QPixmap("userpark.jpg")
        self.splassh=QSplashScreen(self.pix,Qt.WindowStaysOnTopHint)
        self.splassh.show()


def showsetupwindow():
    mainScreen.splassh.close()
    installWindow.show()

def showloginwindow():
    login.showloginscreen()
    mainScreen.splassh.close()



app=QApplication(sys.argv)
mainScreen=MainScreen()
login=loginscreen()
mainScreen.showsplashscreen()
installWindow=InstallWindow()

if os.path.exists("./config.json"):
    QTimer.singleShot(2000,showloginwindow)
else:
    QTimer.singleShot(2000,showsetupwindow)

sys.exit(app.exec_())