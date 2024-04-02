import typing
from PyQt6.QtGui import QIcon
import sys
from PyQt6 import QtGui
import random

from PyQt6.QtWidgets import QMainWindow, QStackedWidget


from Vue.vueCreationEleve import vueCreationEleve
from Vue.vueListeEleves import vueListeEleves
from Vue.vueSecrete import vueSecrete


class pagePrincipale(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Appel")
        self.setWindowIcon(QIcon('images/iconeApp.ico'))

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.resize(500, 350)  # largeur / hauteur


        self.page1 = vueCreationEleve()
        self.page2 = vueListeEleves()
        self.pageesecrete = vueSecrete()

        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        self.stacked_widget.addWidget(self.pageesecrete)


        self.stacked_widget.setCurrentIndex(1)

        self.page1.boutonValider.clicked.connect(lambda: self.changerPage())
        self.page1.boutonRetour.clicked.connect(lambda: self.changerPage())
        self.page2.boutonAjouter.clicked.connect(lambda: self.changerPage())

    def changerPage(self):
        nb = random.randint(0,20)
        #print(nb)
        if nb == 17:
            self.stacked_widget.setCurrentIndex(2)
        else:
            if(self.stacked_widget.currentIndex() == 0):
                self.stacked_widget.setCurrentIndex(1)
                self.page2.modele.setData()
                self.page2.addDataInList()
            else:
                self.stacked_widget.setCurrentIndex(0)
                self.page2.liste.clear()


