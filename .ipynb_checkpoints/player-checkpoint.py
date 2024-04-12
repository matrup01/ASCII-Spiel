import random

class Player:
    def __init__(self):
        self.name = ""
        self.titlename = ""
        self.maxhp = random.randint(10,15)
        self.currenthp = self.maxhp
        self.hastitle = False
        self.titlerep = 0 #0 --> neutral; 1 --> lächerlich; 2 --> heftig
        self.rep = random.randrange(-1,1)  #negativ --> unbeliebt; positiv --> beliebt

    def setname(self,name):
        self.name = name
        self.titlename = name