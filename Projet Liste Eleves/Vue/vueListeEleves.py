from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QTextEdit, QVBoxLayout, QComboBox, \
    QListWidget, QListWidgetItem
from PyQt6.QtGui import QIcon


from Model.modelListeEleve import modelListeEleve
from Controler.controllerListeEleves import controllerListeEleve




class vueListeEleves(QWidget):

    def __init__(self):
        super().__init__()


        #print("blou")
        #self.show()

        self.liste = QListWidget()

        #MVC
        self.modele = modelListeEleve()
        self.controller = controllerListeEleve(self.modele,self)



        layout = QVBoxLayout()
        self.setLayout(layout)



        self.addDataInList()


        self.nomSelec = QLabel()
        self.prenomSelec = QLabel()
        self.classSelec = QLabel()
        self.idSelec = QLabel()

        self.boutonAjouter = QPushButton("Ajouter un élève")
        layout.addWidget(self.liste)

        layout.addWidget(self.nomSelec)
        layout.addWidget(self.prenomSelec)
        layout.addWidget(self.classSelec)
        layout.addWidget(self.idSelec)
        layout.addWidget(self.boutonAjouter)




    def printInfos(self, row):

        infos = self.modele.listeEleves[row]

        self.nomSelec.setText(infos[0])
        self.prenomSelec.setText(infos[1])
        self.classSelec.setText(infos[2])
        self.idSelec.setText("ID: " + infos[3])



    def addDataInList(self):
        for object in self.modele.listeEleves:
            stri = object[0]+ " " + object[1]
            QListWidgetItem(stri, self.liste)