class controllerListeEleve:

    def __init__(self, modele, vue):
        self.modele = modele
        self.vue = vue

        self.vue.liste.itemSelectionChanged.connect(lambda: self.vue.printInfos(self.vue.liste.currentRow()))