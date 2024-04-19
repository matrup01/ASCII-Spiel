import random
import colors
import items

class Player:
    def __init__(self):
        self.name = ""
        self.titlename = ""
        self.gender = 0 #0--> weiblich, 1--> männlich
        self.maxhp = random.randint(10,15)
        self.currenthp = self.maxhp
        self.hastitle = False
        self.titlerep = 0 #-2/-1/0/1/2
        self.xp = 0
        self.currentxp = 0
        self.lvl = 1
        self.colorer = colors.Colormap()
        weaponizer = [random.randrange(3),random.randrange(1,5)]
        if weaponizer[0] == 0:
            self.lweapon = items.Dagger(weaponizer[1],0)
        elif weaponizer[0] == 1:
            self.lweapon = items.Axe(weaponizer[1],0)
        else:
            self.lweapon = items.Sword(weaponizer[1],0)
        self.haslweapon = True
        self.rweapon = items.Weapon(0,0)
        self.hasrweapon = False
        self.armor = items.Armor(0,0)
        self.hasarmor = False
        self.shoes = items.Shoes(0,0)
        self.hasshoes = False
        self.helmet = items.Helmet(0,0)
        self.hashelmet = False
        self.gold = random.randint(3,6)
        self.maxpotions = 3
        self.potions = 3

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
        hplen = len(str(self.currenthp)) + len(str(self.maxhp))
        hplennorm4 = 4 - hplen
        offset = offset + hplennorm4
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

    def equipweapon(self,weapon,forced = False):
        if not forced:
            if not self.haslweapon or not self.hasrweapon:
                weapon.printstats(0)
            else:
                print("Ausgerüstet (Links):")
                self.lweapon.printstats(5)
                print("Ausgerüster (Rechts):")
                self.rweapon.printstats(5)
                print("Neu:")
                weapon.printstats(5)
            choice = input("Waffe ausrüsten? (j/n) >")
        if forced:
            choice = "j"
            if self.haslweapon and self.hasrweapon:
                print("Ausgerüstet (Links):")
                self.lweapon.printstats(5)
                print("Ausgerüster (Rechts):")
                self.rweapon.printstats(5)
                print("Neu:")
                weapon.printstats(5)
        if choice == "j":
            if not self.haslweapon:
                self.haslweapon = True
                self.lweapon = weapon
                print(weapon.name + " wurde links ausgerüstet")
            elif not self.hasrweapon:
                self.hasrweapon = True
                self.rweapon = weapon
                print(weapon.name + " wurde rechts ausgerüstet")
            else:
                lrchoice = input("Links oder Rechts? (l/r) >")
                if lrchoice == "l":
                    self.haslweapon = True
                    self.lweapon = weapon
                    print(weapon.name + " wurde links ausgerüstet")
                elif lrchoice == "r":
                    self.hasrweapon = True
                    self.rweapon = weapon
                    print(weapon.name + " wurde rechts ausgerüstet")
                else:
                    if forced:
                        self.haslweapon = True
                        self.lweapon = weapon
        else:
            print(weapon.name + " wurde nicht ausgerüstet")

    def equiparmor(self,armor,forced = False):
        if not forced:
            if not self.hasarmor:
                armor.printstats(0)
            else:
                print("Ausgerüstet:")
                self.armor.printstats(5)
                print("Neu:")
                armor.printstats(5)
            choice = input("Rüstung ausrüsten? (j/n) >")
        if forced:
            choice = "j"
        if choice == "j":
            self.hasarmor = True
            self.armor = armor
            print(armor.name + " wurde ausgerüstet")
        else:
            print(armor.name + " wurde nicht ausgerüstet")

    def equipshoes(self,shoes,forced = False):
        if not forced:
            if not self.hasshoes:
                shoes.printstats(0)
            else:
                print("Ausgerüstet:")
                self.shoes.printstats(5)
                print("Neu:")
                shoes.printstats(5)
            choice = input("Schuhe ausrüsten? (j/n) >")
        if forced:
            choice = "j"
        if choice == "j":
            self.hasshoes = True
            self.shoes = shoes
            print(shoes.name + " wurden ausgerüstet")
        else:
            print(shoes.name + " wurden nicht ausgerüstet")

    def equiphelmet(self,helmet,forced = False):
        if not forced:
            if not self.hashelmet:
                helmet.printstats(0)
            else:
                print("Ausgerüstet:")
                self.helmet.printstats(5)
                print("Neu:")
                helmet.printstats(5)
            choice = input("Helm ausrüsten? (j/n) >")
        if forced:
            choice = "j"
        if choice == "j":
            self.hashelmet = True
            self.helmet = helmet
            print(helmet.name + " wurde ausgerüstet")
        else:
            print(helmet.name + " wurde nicht ausgerüstet")

    def printequip(self):
        print(self.titlename)
        if self.haslweapon:
            print("     Linke Hand")
            self.lweapon.printstats(5)
        else:
            print("     Linke Hand:   LEER")
        if self.hasrweapon:
            print("     Rechte Hand")
            self.rweapon.printstats(5)
        else:
            print("     Rechte Hand:  LEER")
        if self.hasarmor:
            self.armor.printstats(5)
        else:
            print("     Rüstung:      LEER")
        if self.hasshoes:
            self.shoes.printstats(5)
        else:
            print("     Schuhe:       LEER")
        if self.hashelmet:
            self.helmet.printstats(5)
        else:
            print("     Helm:         LEER")
