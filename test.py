from _typeshed import Self
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class Modbus(QDialog):
    def __init__(self):
        super(Modbus,self).__init__()
        loadUi('version_1.ui',self)
        
app = QApplication(sys.argv)
window=Modbus()
widget=QtWidgets.QStackedWidget()
widget.addWidget(window)
widget.setFixedWidth((1920/3)*2)
widget.setFixedHeight((1080/10)*8)
widget.show()
app.exec_()