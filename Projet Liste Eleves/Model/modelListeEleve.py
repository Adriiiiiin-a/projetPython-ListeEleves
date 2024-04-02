import csv

class modelListeEleve:

    def __init__(self):

        self.listeEleves = []
        self.setData()

    def clearList(self):
        self.listeEleves=[]

    def setData(self):

        self.clearList()

        f = open('data/data.csv', 'r')

        reader = csv.reader(f)

        for row in reader:
            self.listeEleves.append(row)


        f.close()

        #print(self.listeEleves)

