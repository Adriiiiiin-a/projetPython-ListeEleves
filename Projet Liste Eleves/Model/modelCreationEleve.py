import csv


class ModelCreationEleve:

    def __init__(self):
        self.o = 0


    def getLastStudentNumber(self):
        listE = []
        f = open('data/data.csv', 'r')

        reader = csv.reader(f)

        for row in reader:
            listE.append(row)


        taille = len(listE)

        #print(listE[taille-1][3])
        f.close()
        return(listE[(taille-1)][3])




    def ajoutEleveBase(self, data = []):

        #print(data)

        data.append(int(self.getLastStudentNumber())+1)

        # open the file in the write mode
        f = open('data/data.csv', 'a', newline='')

        # create the csv writer
        writer = csv.writer(f)

        # write a row to the csv file
        writer.writerow(data)

        # close the file
        f.close()