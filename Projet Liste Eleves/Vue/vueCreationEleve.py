from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QTextEdit, QVBoxLayout,QComboBox
from PyQt6.QtGui import QIcon
from Model.modelCreationEleve import ModelCreationEleve
from Controler.controllerCreationEleve import controllerCreationEleve
from Vue.vueListeEleves import vueListeEleves


class vueCreationEleve(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Appel - Ajouter un élève")
        self.setWindowIcon(QIcon('images/iconeApp.ico'))

        #self.show()


        #MVC
        self.modele = ModelCreationEleve()
        self.controller = controllerCreationEleve(self.modele)

        # Layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Widgets
        self.inputPrenom = QLineEdit("Prénom")
        self.inputNom = QLineEdit("Nom")
        self.listeClasses = QComboBox()

        self.listeClasses.addItem("SNPI3")
        self.listeClasses.addItem("SNPI4")
        self.listeClasses.addItem("SNPI5")
        self.listeClasses.addItem("SEE3")
        self.listeClasses.addItem("SEE4")
        self.listeClasses.addItem("SEE5")
        self.listeClasses.addItem("Enseignant")



        self.boutonValider = QPushButton("Enregistrer",
                                         clicked=lambda:self.change())
        self.boutonRetour = QPushButton("Retour")

        layout.addWidget(self.inputPrenom)
        layout.addWidget(self.inputNom)
        layout.addWidget(self.listeClasses)
        layout.addWidget(self.boutonValider)
        layout.addWidget(self.boutonRetour)




    def change(self):

            self.controller.enregistrerEleve(self.inputNom.text(),
                                                 self.inputPrenom.text(), self.listeClasses.currentText())


