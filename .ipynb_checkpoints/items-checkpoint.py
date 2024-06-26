import colors
import namegenerator
import numpy as np
import random

class Weapon:                                      #Weapons
    def __init__(self,power,rareness):
        self.rareness = rareness
        self.power = power
        self.stats = np.array([0,0,0.5,0,0,0,0,0,0,0,0,0]) #0-->atk, 1-->def, 2-->acc, 3--> poison, 4--> burn, 5--> blut, 6--> reflect, 7--> thorns, 8--> stun, 9-->spezialeffekt, 10--> life steal, 11-->upgradetimes
        self.colorer = colors.Colormap()
        self.namegen = namegenerator.Names()
        self.name = ""
        self.type = ""
        self.hasname = False
        

    def printstats(self,off):
        offset = off * " "
        print(offset + self.name + ":")
        offset += 5 * " "
        if self.stats[0] > 0:
            print(offset + "Angriff:      " + str(self.stats[0]))
        if self.stats[1] > 0:
            print(offset + "Verteidigung: " + str(self.stats[1]))
        if self.stats[3] > 0:
            print(offset + self.colorer.returncolor("Gift:         ",4) + str(self.stats[3]))
        if self.stats[4] > 0:
            print(offset + self.colorer.returncolor("Feuer:        ",2) + str(self.stats[4]))
        if self.stats[5] > 0:
            print(offset + self.colorer.returncolor("Blutung:      ",3) + str(self.stats[5]))
        if self.stats[6] > 0:
            prozentreflekt = int(round(self.stats[6] * 100,0))
            print(offset + self.colorer.returncolor("Reflektieren: ",13) + str(prozentreflekt) + "%")
        if self.stats[7] > 0:
            print(offset + self.colorer.returncolor("Dornen:       ",11) + str(self.stats[7]))
        if self.stats[8] > 0 :
            prozentstun = int(round(self.stats[8] * 100,0))
            print(offset + self.colorer.returncolor("Betäubung:    ",14) + str(prozentstun) + "%")
        if self.stats[9] == 1:
            print(offset + self.colorer.returncolor("Giftheilung",4))
        if self.stats[10] > 0:
            prozentls = int(round(self.stats[10] * 100,0))
            print(offset + self.colorer.returncolor("Lebensentzug: ",3) + str(prozentls) + "%")
        

class Sword(Weapon):
    def __init__(self,power,rareness):
        super().__init__(power,rareness)
        self.type = "off"
        self.stats[0] = self.power
        if self.rareness == 3:
            self.hasname = True
            self.name = self.colorer.returncolor(self.namegen.swordname(),6)
            self.name += self.colorer.returncolor(" (Legendäres Schwert)",6)
        elif self.rareness == 2:
            self.name = self.colorer.returncolor("Schwert",9)
        elif self.rareness == 1:
            self.name = self.colorer.returncolor("Schwert",5)
        else:
            self.name = "Schwert"
        self.stats[2] = 0.95
        for i in range(self.rareness):
            choice = random.randrange(4)
            j = i + 1
            if choice == 0:
                self.stats[3] += j
            elif choice == 1:
                self.stats[4] += j
            elif choice == 2:
                self.stats[5] += j
            elif choice == 3:
                self.stats[0] += 2 * j

    def addpower(self,n):
        self.stats[0] += n
        self.power += n

    def setpower(self):
        self.stats[0] = self.power

    def shufflestats(self):
        self.stats[0] = self.power
        self.stats[3] = 0
        self.stats[4] = 0
        self.stats[5] = 0
        for i in range(self.rareness):
            choice = random.randrange(4)
            j = i + 1
            if choice == 0:
                self.stats[3] += j
            elif choice == 1:
                self.stats[4] += j
            elif choice == 2:
                self.stats[5] += j
            elif choice == 3:
                self.stats[0] += 2 * j

class Shield(Weapon):
    def __init__(self,power,rareness):
        super().__init__(power,rareness)
        self.stats[1] = self.power
        self.type = "def"
        if self.rareness == 3:
            self.hasname = True
            self.name = self.colorer.returncolor(self.namegen.shieldname(),6)
            self.name += self.colorer.returncolor(" (Legendärer Schild)",6)
        elif self.rareness == 2:
            self.name = self.colorer.returncolor("Schild",9)
        elif self.rareness == 1:
            self.name = self.colorer.returncolor("Schild",5)
        else:
            self.name = "Schild"
        self.stats[2] = 0.95
        for i in range(self.rareness):
            choice = random.randrange(3)
            j = i + 1
            if choice == 0:
                self.stats[6] += j * 0.5
            elif choice == 1:
                self.stats[7] += j
            elif choice == 2:
                self.stats[1] += j

    def addpower(self,n):
        self.stats[1] += n
        self.power += n

    def setpower(self):
        self.stats[1] = self.power

    def shufflestats(self):
        self.stats[6] = 0
        self.stats[7] = 0
        for i in range(self.rareness):
            choice = random.randrange(2)
            j = i + 1
            if choice == 0:
                self.stats[6] += j * 0.5
            elif choice == 1:
                self.stats[7] += j

class Axe(Weapon):
    def __init__(self,power,rareness):
        super().__init__(power,rareness)
        self.type = "off"
        self.stats[0] = self.power
        if self.rareness == 3:
            self.hasname = True
            self.name = self.colorer.returncolor(self.namegen.axename(),6)
            self.name += self.colorer.returncolor(" (Legendäre Axt)",6)
        elif self.rareness == 2:
            self.name = self.colorer.returncolor("Axt",9)
        elif self.rareness == 1:
            self.name = self.colorer.returncolor("Axt",5)
        else:
            self.name = "Axt"
        self.stats[2] = 0.9
        for i in range(self.rareness):
            choice = random.randrange(3)
            j = i + 1
            if choice == 0:
                self.stats[5] += j
            elif choice == 1:
                self.stats[8] += 0.2
            elif choice == 2:
                self.stats[0] += (2 * j)

    def addpower(self,n):
        self.stats[0] += n
        self.power += n

    def setpower(self):
        self.stats[0] = self.power

    def shufflestats(self):
        self.stats[0] = self.power
        self.stats[5] = 0
        self.stats[8] = 0
        for i in range(self.rareness):
            choice = random.randrange(3)
            j = i + 1
            if choice == 0:
                self.stats[5] += j
            elif choice == 1:
                self.stats[8] += 1
            elif choice == 2:
                self.stats[0] += (2 * j)

class Dagger(Weapon):
    def __init__(self,power,rareness):
        super().__init__(power,rareness)
        self.type = "off"
        self.stats[0] = self.power
        if self.rareness == 3:
            self.hasname = True
            self.name = self.colorer.returncolor(self.namegen.daggername(),6)
            self.name += self.colorer.returncolor(" (Legendärer Dolch)",6)
        elif self.rareness == 2:
            self.name = self.colorer.returncolor("Dolch",9)
        elif self.rareness == 1:
            self.name = self.colorer.returncolor("Dolch",5)
        else:
            self.name = "Dolch"
        self.stats[2] = 0.9
        for i in range(self.rareness):
            choice = random.randrange(3)
            j = i + 1
            if choice == 0:
                self.stats[3] += j
            elif choice == 1:
                k = 1 / random.randrange(8,11)
                self.stats[10] += j * k
                self.stats[10] = round(self.stats[10],3)
            elif choice == 2:
                self.stats[5] += j
            elif choice == 2:
                self.stats[0] += (3 * j)

    def addpower(self,n):
        self.stats[0] += n
        self.power += n

    def setpower(self):
        self.stats[0] = self.power

    def shufflestats(self):
        self.stats[0] = self.power
        self.stats[3] = 0
        self.stats[5] = 0
        self.stats[10] = 0

class Armor:
    def __init__(self,power,rareness):
        self.rareness = rareness
        if self.rareness == 0:
            self.defense = int(round(power * 0.5,0))
        else:
            self.defense = power * self.rareness
        self.name = ""
        self.colorer = colors.Colormap()
        self.upgradetimes = 0
        if self.rareness == 3:
            self.name = self.colorer.returncolor("Legendäre Rüstung",6)
        elif self.rareness == 2:
            self.name = self.colorer.returncolor("Rüstung",9)
        elif self.rareness == 1:
            self.name = self.colorer.returncolor("Rüstung",5)
        else:
            self.name = "Rüstung"

    def printstats(self,off):
        offset = off * " "
        print(offset + self.name + ":")
        offset += 5 * " "
        print(offset + "Verteidigung: " + str(self.defense))

class Shoes:
    def __init__(self,power,rareness):
        self.rareness = rareness
        self.speed = power * self.rareness
        self.name = ""
        self.colorer = colors.Colormap()
        self.upgradetimes = 0
        if self.rareness == 3:
            self.name = self.colorer.returncolor("Legendäre Schuhe",6)
        elif self.rareness == 2:
            self.name = self.colorer.returncolor("Schuhe",9)
        elif self.rareness == 1:
            self.name = self.colorer.returncolor("Schuhe",5)
        else:
            self.name = "Schuhe"

    def printstats(self,off):
        offset = off * " "
        print(offset + self.name + ":")
        offset += 5 * " "
        print(offset + "Geschwindigkeit: " + str(self.speed))

class Helmet:
    def __init__(self,power,rareness):
        self.rareness = rareness
        self.defense = power
        self.evasiveness = self.rareness * 0.1
        self.name = ""
        self.colorer = colors.Colormap()
        self.upgradetimes = 0
        if self.rareness == 3:
            self.name = self.colorer.returncolor("Legendärer Helm",6)
        elif self.rareness == 2:
            self.name = self.colorer.returncolor("Helm",9)
        elif self.rareness == 1:
            self.name = self.colorer.returncolor("Helm",5)
        else:
            self.name = "Helm"

    def printstats(self,off):
        offset = off * " "
        print(offset + self.name + ":")
        offset += 5 * " "
        print(offset + "Verteidigung: " + str(self.defense))
        prozentevasiveness = round(self.evasiveness * 100,1)
        print(offset + "Ausweichwert: " + str(prozentevasiveness) + "%")
        
        