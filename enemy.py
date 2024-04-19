import items
import colors
import random

class Enemy:
    def __init__(self,hp,name):
        self.maxhp = hp
        self.name = name
        self.currenthp = hp
        self.lweapon = items.Weapon(0,0)
        self.haslweapon = False
        self.rweapon = items.Weapon(0,0)
        self.hasrweapon = False
        self.armor = items.Armor(0,1)
        self.hasarmor = False
        self.shoes = items.Shoes(0,0)
        self.hasshoes = False
        self.helmet = items.Helmet(0,0)
        self.hashelmet = False
        self.colorer = colors.Colormap()
        self.show = [False,False,False,False,False]
        self.stats = [0,0,0,0,0,0,0,0,0,0,0,0]
        self.evasiveness = 0
        self.speed = 0
        self.addinfo = ""
        self.xp = 5

    def equipsword(self,name,atk,pos = "l",color = 16,acc = 0.95,poison = 0,burn = 0,blut = 0,stun = 0,spezial = 0,lifesteal = 0,hidden = False):
        if pos == "l":
            if not hidden:
                self.show[0] = True
            self.haslweapon = True
            self.lweapon = items.Sword(0,0)
            self.lweapon.name = self.colorer.returncolor(name,color)
            self.lweapon.power = atk
            self.lweapon.stats = [atk,0,acc,poison,burn,blut,0,0,stun,spezial,lifesteal,0]
        else:
            if not hidden:
                self.show[0] = True
            self.hasrweapon = True
            self.rweapon = items.Sword(0,0)
            self.rweapon.name = self.colorer.returncolor(name,color)
            self.rweapon.power = atk
            self.rweapon.stats = [atk,0,acc,poison,burn,blut,0,0,stun,spezial,lifesteal,0]

    def equipshield(self,name,defense,pos = "r",color = 16,acc = 0.95,reflect = 0,thorns = 0,spezial = 0,hidden = False):
        if self.pos == "l":
            if not hidden:
                self.show[1] = True
            self.haslweapon = True
            self.lweapon = items.Shield(0,0)
            self.lweapon.name = self.returncolor(name,color)
            self.lweapon.power = defense
            self.lweapon.stats = [0,defense,acc,0,0,0,reflect,thorns,0,spezial,0,0]
        else:
            if not hidden:
                self.show[1] = True
            self.hasrweapon = True
            self.rweapon = items.Shield(0,0)
            self.rweapon.name = self.returncolor(name,color)
            self.rweapon.power = defense
            self.rweapon.stats = [0,defense,acc,0,0,0,reflect,thorns,0,spezial,0,0]

    def equiparmor(self,name,defense,color = 16,hidden = False):
        if not hidden:
                self.show[2] = True
        self.hasarmor = True
        self.armor.defense = defense
        self.armor.name = colorer.returncolor(name,color)

    def equipshoes(self,name,speed,color = 16,hidden = False):
        if not hidden:
                self.show[3] = True
        self.hasshoes = True
        self.shoes.speed = speed
        self.shoes.name = colorer.returncolor(name,color)

    def equiphelmet(self,name,defense,evasiveness,color = 16,hidden = False):
        if not hidden:
                self.show[4] = True
        self.hashelmet = True
        self.helmet.defense = defense
        self.helmet.evasiveness = evasivensee
        self.helmet.name = colorer.returncolor(name,color)

    def printstats(self):
        print(self.name)
        print(self.addinfo)
        if self.show[0]:
            print("     Linke Hand")
            self.lweapon.printstats(5)
        if self.show[1]:
            print("     Rechte Hand")
            self.rweapon.printstats(5)
        if self.show[2]:
            self.armor.printstats(5)
        if self.show[3]:
            self.shoes.printstats(5)
        if self.show[4]:
            self.helmet.printstats(5)

    def loot(self,player):
        equip = [1,2,3,4,5]
        weights = [0,0,0,0,0]
        for i in range(len(self.show)):
            if self.show[i]:
                weights[i] = 1
        loot = random.choices(equip,weights=weights)
        print("Test")
        if loot == 1:
            print("Der Gegner hat eine seiner Waffen fallen gelassen")
            player.equipweapon(self.lweapon)
        elif loot == 2:
            print("Der Gegner hat eine seiner Waffen fallen gelassen")
            player.equipweapon(self.rweapon)
        elif loot == 3:
            print("Der Gegner hat seine Rüstung fallen gelassen")
            player.equiparmor(self.armor)
        elif loot == 4:
            print("Der Gegner hat seine Schuhe fallen gelassen")
            player.equipshoes(self.shoes)
        elif loot == 5:
            print("Der Gegner hat seinen Helm fallen gelassen")
            player.equiphelmet(self.helmet)

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