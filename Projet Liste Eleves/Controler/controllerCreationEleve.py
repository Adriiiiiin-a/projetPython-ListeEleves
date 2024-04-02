class controllerCreationEleve:

    def __init__(self, modele):
        self.modele = modele




    def enregistrerEleve(self, nom, prenom,classe):

        data = [nom,prenom,classe]
        #print(data)
        self.modele.ajoutEleveBase(data)



