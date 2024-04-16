import items
import player
import random
import time

class Blacksmith:
    def __init__(self,player):
        self.player = player
        self.rarenesschecker = False
        self.cost = random.randrange(3,7)
        self.eff = random.randrange(1,4)
        self.leave = False
        rarenesssum = player.lweapon.rareness + player.rweapon.rareness + player.armor.rareness + player.shoes.rareness + player.helmet.rareness
        if rarenesssum > 0:
            self.rarenesschecker = True

    def offers(self):
        print("Angebote:")
        print("     1. Verstärke einen Gegenstand")
        print("     2. Würfle die Boni eines Gegenstands neu")
        print("     3. Verlassen")
        choice = input(">")
        if choice == "1":
            self.upgrade()
        elif choice == "2":
            self.reshuffle()
        elif choice == "3":
            self.leave = True
            pass
        else:
            pass

    def upgrade(self):
        i = 1
        lweaponindex = 101
        rweaponindex = 102
        armorindex = 103
        shoesindex = 104
        helmetindex = 105
        print("Erhöhe den Primärwert einer Ausrüstung um " + str(self.eff))
        print("")
        if self.player.haslweapon:
            lweaponindex = i
            print(str(i) + ". (" + str(self.cost) + " Gold)")
            self.player.lweapon.printstats(2)
            i += 1
        if self.player.hasrweapon:
            rweaponindex = i
            print(str(i) + ". (" + str(self.cost) + " Gold)")
            self.player.rweapon.printstats(2)
            i += 1
        if self.player.hasarmor:
            armorindex = i
            print(str(i) + ". (" + str(self.cost) + " Gold)")
            self.player.armor.printstats(2)
            i += 1
        if self.player.hasshoes:
            shoesindex = i
            print(str(i) + ". (" + str(self.cost) + " Gold)")
            self.player.shoes.printstats(2)
            i += 1
        if self.player.hashelmet:
            helmetindex = i
            print(str(i) + ". (" + str(self.cost) + " Gold)")
            self.player.helmet.printstats(2)
            i += 1
        print("")
        opt = input(">")
        if opt == "1" or opt == "2" or opt == "3" or opt == "4" or opt == "5":
            checker = int(opt)
            if self.player.gold < self.cost:
                print("Nicht genug Gold!")
                time.sleep(2)
                pass
            elif checker == lweaponindex:
                self.player.gold -= self.cost
                self.player.lweapon.addpower(self.eff)
                if self.player.lweapon.stats[11] == 0:
                    self.player.lweapon.name += " +1"
                    self.player.lweapon.stats[11] += 1
                else:
                    self.player.lweapon.name = self.player.lweapon.name.rstrip(str(int(self.player.lweapon.stats[11])))
                    self.player.lweapon.stats[11] += 1
                    self.player.lweapon.name += str(int(self.player.lweapon.stats[11]))
            elif checker == rweaponindex:
                self.player.gold -= self.cost
                self.player.rweapon.addpower(self.eff)
                if self.player.rweapon.stats[11] == 0:
                    self.player.rweapon.name += " +1"
                    self.player.rweapon.stats[11] += 1
                else:
                    self.player.rweapon.name = self.player.rweapon.name.rstrip(str(int(self.player.rweapon.stats[11])))
                    self.player.rweapon.stats[11] += 1
                    self.player.rweapon.name += str(int(self.player.rweapon.stats[11]))
            elif checker == armorindex:
                self.player.gold -= self.cost
                self.player.armor.defense += 1
                if self.player.armor.upgradetimes == 0:
                    self.player.armor.name += " +1"
                    self.player.armor.upgradetimes += 1
                else:
                    self.player.armor.name = self.player.armor.name.rstrip(str(int(self.player.armor.upgradetimes)))
                    self.player.armor.upgradetimes += 1
                    self.player.armor.name += str(int(self.player.armor.upgradetimes))
            elif checker == shoesindex:
                self.player.gold -= self.cost
                self.player.shoes.speed += 1
                if self.player.shoes.upgradetimes == 0:
                    self.player.shoes.name += " +1"
                    self.player.shoes.upgradetimes += 1
                else:
                    self.player.shoes.name = self.player.shoes.name.rstrip(str(int(self.player.shoes.upgradetimes)))
                    self.player.shoes.upgradetimes += 1
                    self.player.shoes.name += str(int(self.player.shoes.upgradetimes))
            elif checker == helmetindex:
                self.player.gold -= self.cost
                self.player.helmet.defense += 1
                if self.player.helmet.upgradetimes == 0:
                    self.player.helmet.name += " +1"
                    self.player.helmet.upgradetimes += 1
                else:
                    self.player.helmet.name = self.player.helmet.name.rstrip(str(int(self.player.helmet.upgradetimes)))
                    self.player.helmet.upgradetimes += 1
                    self.player.helmet.name += str(int(self.player.helmet.upgradetimes))
            else:
                pass

    def reshuffle(self):
        i = 1
        lweaponindex = 101
        rweaponindex = 102
        armorindex = 103
        shoesindex = 104
        helmetindex = 105
        print("Würfelt die Effekte einer Ausrüstung neu")
        print("")
        if self.player.haslweapon and self.player.lweapon.rareness > 0:
            lweaponindex = i
            print(str(i) + ". (2 Gold)")
            self.player.lweapon.printstats(2)
            i += 1
        if self.player.hasrweapon and self.player.rweapon.rareness > 0:
            rweaponindex = i
            print(str(i) + ". (2 Gold)")
            self.player.rweapon.printstats(2)
            i += 1
        if i == 1:
            print("Keine geeignete Ausrüstung gefunden...")
            time.sleep(2)
            pass
        else:
            print("")
            opt = input(">")
            if opt == "1" or opt == "2":
                checker = int(opt)
                if self.player.gold < 2:
                    print("Nicht genug Gold!")
                    time.sleep(1)
                    pass
                elif checker == lweaponindex:
                    self.player.gold -= 2
                    self.player.lweapon.shufflestats()
                elif checker == rweaponindex:
                    self.player.gold -= 2
                    self.player.rweapon.shufflestats()
                else:
                    pass