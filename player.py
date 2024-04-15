import random
import colors

class Player:
    def __init__(self):
        self.name = ""
        self.titlename = ""
        self.gender = 0 #0--> weiblich, 1--> männlich
        self.maxhp = random.randint(10,15)
        self.currenthp = self.maxhp
        self.hastitle = False
        self.titlerep = 0 #0 --> neutral; 1 --> lächerlich; 2 --> heftig
        self.rep = random.randrange(-1,1)  #negativ --> unbeliebt; positiv --> beliebt
        self.xp = 0
        self.currentxp = 0
        self.lvl = 1
        self.colorer = colors.Colormap()

    def setname(self,name):
        self.name = name
        self.titlename = name

    def setgender(self,gender):
        if gender == "W" or gender == "F":
            self.gender = 0
        if gender == "M":
            self.gender = 1

    def earnxp(self,xp):
        loop = True
        self.xp += xp
        self.currentxp += xp
        while loop:
            tester = self.lvl * 30
            if self.currentxp >= tester:
                self.currentxp -= tester
                self.lvl += 1
                hpgain = random.randrange(2,5)
                self.currenthp += hpgain
                self.maxhp += hpgain
            else:
                return

    def gethealthbar(self,offset,length):
        relhp = self.currenthp / self.maxhp
        tylecounter = (length - 2) * relhp
        tylecounter = int(round(tylecounter))
        dashcounter = length - 2 - tylecounter
        output = offset * " "
        output += "|"
        output += self.colorer.returncolor(" ",17) * tylecounter
        output += "-" * dashcounter
        output += "|"
        return output

    def getxpbar(self,offset,length):
        if self.xp >= 1000:
            offset -= 3
        elif self.xp >= 100:
            offset -= 2
        elif self.xp >= 10:
            offset -= 1
        relxp = self.currentxp / (self.lvl * 30)
        tylecounter = (length - 2) * relxp
        tylecounter = int(round(tylecounter))
        dashcounter = length - 2 - tylecounter
        output = offset * " "
        output += "|"
        output += self.colorer.returncolor(" ",18) * tylecounter
        output += "-" * dashcounter
        output += "|"
        return output