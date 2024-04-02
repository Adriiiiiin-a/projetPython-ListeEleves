import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QTextEdit, QVBoxLayout
from Vue.pagePrincipale import *

app = QApplication([])
app.setStyleSheet('''
QWidget {

    font-size: 17px;

}

QPushButton {

    font-size: 30px;

}

''')

window = pagePrincipale()
window.show()




app.exec()