import random

class Event:
    def __init__(self): #Übersicht über Typletypes @ tyletypes.txt
        self.options = [0,1,2,3,4,5]
        self.status = [0,0,0,0,0]          #status inputs: 0--> playerx, 1--> playery, 2--> tyletype, 3 --> newcell(immer true), 4 --> Anzahl besuchte Felder

    def select(self,status): #gibt ein Event aus (je nach tyletype unterschiedlich gewichtet) 0 --> Kampf, 1 --> Händler, 2--> randevent, 3 --> Schatz, 4--> Boss, 5--> Schmied
        self.status = status
        if self.status[4] == 210:
            select = 4
        else:
            if status[2] == 0:
                weight = [1,1,1,1,1,1]
            elif status[2] == 1:
                weight = [0,1,0,0,0,0]
            else:
                weight = [1,1,1,1,1,1]
            selectlist = random.choices(self.options,weights=weight)
            select = selectlist[0]
        return select
        