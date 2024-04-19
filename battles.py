import random
import namegenerator
import player
import enemy
import items
import colors

class Battler:
    def __init__(self,player):
        self.colorer = colors.Colormap()
        self.stillgoing = True
        self.phase = 0  #0...EnemyTurn,1...PlayerTurn,2...EnemyDefeated
        self.player = player
        self.enemy = enemy.Enemy(5,"Platzhalter")
        self.playerstats = [0,0,0,0,0,0,0,0,0,0,0,0]
        self.enemystats  = [0,0,0,0,0,0,0,0,0,0,0,0]
        self.playershield = 0
        self.enemyshield = 0
        self.noclear = False
        self.loot = True

    def set(self,enemy,player,loot = True):
        self.stillgoing = True
        self.player = player
        self.enemy = enemy
        self.playerstats = [0,0,0,0,0,0,0,0,0,0,0,0]
        self.enemystats  = [0,0,0,0,0,0,0,0,0,0,0,0]
        self.playershield = 0
        self.enemyshield = 0
        self.noclear = False
        self.loot = loot

    def battleheader(self):
        p = self.player.titlename + ": "
        if self.playerstats[3] != 0:
            p += self.colorer.returncolor("G" + str(self.playerstats[3]) + " ",4)
        if self.playerstats[4] != 0:
            p += self.colorer.returncolor("F" + str(self.playerstats[4]) + " ",2)
        if self.playerstats[5] != 0:
            p += self.colorer.returncolor("B" + str(self.playerstats[5]) + " ",3)
        if self.playerstats[6] != 0:
            prozent = int(round(self.playerstats[6] * 100),0)
            p += self.colorer.returncolor("R" + str(prozent) + "% ",13)
        if self.playerstats[7] != 0:
            p += self.colorer.returncolor("D" + str(self.playerstats[7]) + " ",11)
        if self.playerstats[8] != 0:
            p += self.colorer.returncolor("B" + str(self.playerstats[14]) + " ",14)
        if self.playerstats[10] != 0:
            prozent  = int(round(self.playerstats[10] * 100),0)
            p += self.colorer.returncolor("L" + st(prozent) + " ",3)
        print(p)
        print(self.player.gethealthbar(0,30))
        e = self.enemy.name + ": "
        if self.enemystats[3] != 0:
            e += self.colorer.returncolor("G" + str(self.enemystats[3]) + " ",4)
        if self.enemystats[4] != 0:
            e += self.colorer.returncolor("F" + str(self.enemystats[4]) + " ",2)
        if self.enemystats[5] != 0:
            e += self.colorer.returncolor("B" + str(self.enemystats[5]) + " ",3)
        if self.enemystats[6] != 0:
            prozent = int(round(self.enemystats[6] * 100),0)
            e += self.colorer.returncolor("R" + str(prozent) + "% ",13)
        if self.enemystats[7] != 0:
            e += self.colorer.returncolor("D" + str(self.enemystats[7]) + " ",11)
        if self.enemystats[8] != 0:
            e += self.colorer.returncolor("B" + str(self.enemystats[14]) + " ",14)
        if self.enemystats[10] != 0:
            prozent  = int(round(self.enemystats[10] * 100),0)
            e += self.colorer.returncolor("L" + st(prozent) + " ",3)
        print(e)
        print(self.enemy.gethealthbar(0,30))

    def run(self):
        if self.phase == 0:
            self.enemyturn()
            self.noclear = True
        elif self.phase == 1:
            self.playerturn()
            self.noclear = False
        elif self.phase == 2:
            self.end()
            self.noclear = False
            self.stillgoing = False
                                          

    def enemyturn(self):
        self.battleheader()
        if self.enemy.haslweapon and self.enemy.hasrweapon:
            choice = random.randrange(2)
        elif self.enemy.haslweapon and not self.enemy.hasrweapon:
            choice = 0
        elif self.enemy.hasrweapon and not self.enemy.haslweapon:
            choice = 1
        else:
            choice = 3
            damage = 0
        if choice == 0 and self.enemy.lweapon.type == "off":
            evs = (1 - self.enemy.lweapon.stats[2]) + (1 - self.enemy.lweapon.stats[2]) * self.player.helmet.evasiveness
            if random.random() >= evs:
                damage = self.enemy.stats[0] + self.enemy.lweapon.stats[0] - self.playershield - self.player.armor.defense - self.player.helmet.defense
                atk = self.enemy.stats[0] + self.enemy.lweapon.stats[0]
                block = self.playershield + self.player.armor.defense + self.player.helmet.defense
                print(self.enemy.name + "greift dich mit " + self.enemy.lweapon.name)
                print("an und fügt dir " + str(atk) + " Schaden zu, wobei du " + str(block) + " davon abwehren kannst")
                self.player.currenthp -= damage
                self.playershield = 0
            else:
                print("Der Angriff des Gegners hat sein Ziel verfehlt.")
                damage = 0
                self.playershield = 0
        elif choice == 1 and self.enemy.rweapon.type == "off":
            evs = (1 - self.enemy.rweapon.stats[2]) + (1 - self.enemy.rweapon.stats[2]) * self.player.helmet.evasiveness
            if random.random() >= evs:
                damage = self.enemy.stats[0] + self.enemy.rweapon.stats[0] - self.playershield - self.player.armor.defense - self.player.helmet.defense
                atk = self.enemy.stats[0] + self.enemy.lweapon.stats[0]
                block = self.playershield + self.player.armor.defense + self.player.helmet.defense
                print(self.enemy.name + "greift dich mit " + self.enemy.lweapon.name)
                print("an und fügt dir " + str(atk) + " Schaden zu, wobei du " + str(block) + " davon abwehren kannst")
                self.player.currenthp -= damage
                self.playershield = 0
            else:
                print("Der Angriff des Gegners hat sein Ziel verfehlt.")
                self.playershield = 0
                damage = 0
        elif choice == 0 and self.enemy.lweapon.type == "def":
            self.enemyshield = self.enemy.lweapon.stats[1]
            print(self.enemy.name + "geht hinter seinem " + self.enemy.lweapon.name + " in Deckung.")
            self.playershield = 0
        elif choice == 1 and self.enemy.rweapon.type == "def":
            self.enemyshield = self.enemy.rweapon.stats[1]
            print(self.enemy.name + "geht hinter seinem " + self.enemy.rweapon.name + " in Deckung.")
            self.playershield = 0
        if self.enemy.currenthp <= 0:
            self.phase = 2
        else:
            self.phase = 1

    def playerturn(self):
        self.battleheader()
        options = input("Wie gehst du vor? >")
        if options == "o":
            print("o        ...   Zeigt alle möglichen Befehle an")
            print("i        ...   Zeigt das eigene Inventar an")
            print("e        ...   Zeigt Informationen über den Gegner an")
            print("h        ...   Verwende einen Heiltrank")
            print("l        ...   Nutze die Waffe in der linken Hand")
            print("r        ...   Nutze die Waffe in der rechten Hand")
            input()
            return
        elif options == "i":
            self.player.printequip()
            input()
            return
        elif options == "e":
            self.enemy.printstats()
            input()
            return
        elif options == "h":
            if self.player.potions > 0:
                self.player.currenthp = self.player.maxhp
                self.player.potions -= 1
                self.enemyshield = 0
                print("Du hast deine HP mit einem Heiltrank aufgefrischt")
                if self.enemy.currenthp <= 0:
                    self.phase = 2
                    return
                else:
                    self.phase = 0
                    return
            else: 
                return
        elif options == "l":
            if self.player.haslweapon:
                if self.player.lweapon.type == "off":
                    evs = (1 - self.player.lweapon.stats[2]) + (1 - self.player.lweapon.stats[2]) * (self.enemy.helmet.evasiveness + self.enemy.evasiveness)
                    if random.random() >= evs:
                        damage = self.player.lweapon.stats[0] - self.enemyshield - self.enemy.armor.defense - self.enemy.helmet.defense - self.enemy.stats[1]
                        atk = self.player.lweapon.stats[0]
                        block = self.enemyshield + self.enemy.armor.defense + self.enemy.helmet.defense + self.enemy.stats[1]
                        print("Du fügst " + self.enemy.name)
                        print(str(atk) + " Schaden zu, wobei " + str(block) + " davon abgeblockt werden")
                        self.enemy.currenthp -= damage
                    else:
                        print("Der Angriff des Gegners hat sein Ziel verfehlt.")
                        damage = 0
                    self.enemyshield = 0
                    input(">")
                elif self.player.lweapon.type == "def":
                    self.playershield = self.player.lweapon.stats[1]
                    print("Du gehst hinter deinem " + self.player.lweapon.name + " in Deckung")
                    self.enemyshield = 0
                    input(">")
                if self.enemy.currenthp <= 0:
                    self.phase = 2
                    return
                else:
                    self.phase = 0
                    return
            else:
                return
            input()
        elif options == "r":
            if self.player.hasrweapon:
                if self.player.rweapon.type == "off":
                    evs = (1 - self.player.rweapon.stats[2]) + (1 - self.player.rweapon.stats[2]) * (self.enemy.helmet.evasiveness + self.enemy.evasiveness)
                    if random.random() >= evs:
                        damage = self.player.rweapon.stats[0] - self.enemyshield - self.enemy.armor.defense - self.enemy.helmet.defense - self.enemy.stats[1]
                        atk = self.player.lweapon.stats[0]
                        block = self.enemyshield + self.enemy.armor.defense + self.enemy.helmet.defense + self.enemy.stats[1]
                        print("Du fügst " + self.enemy.name)
                        print(str(atk) + " Schaden zu, wobei " + str(block) + " davon abgeblockt werden")
                        self.enemy.currenthp -= damage
                    else:
                        print("Der Angriff des Gegners hat sein Ziel verfehlt.")
                        damage = 0
                    self.enemyshield = 0
                    input(">")
                elif self.player.lweapon.type == "def":
                    self.playershield = self.player.rweapon.stats[1]
                    print("Du gehst hinter deinem " + self.player.rweapon.name + " in Deckung")
                    self.enemyshield = 0
                    input(">")
                if self.enemy.currenthp <= 0:
                    self.phase = 2
                    return
                else:
                    self.phase = 0
                    return
            else:
                return

    def end(self):
        print("Du hast " + self.enemy.name + " besiegt, du erhältst " + str(self.enemy.xp) + "XP")
        input(">")
        self.player.earnxp(self.enemy.xp)
        rand = random.randrange(2)
        if rand == 1:
            if self.loot:
                self.enemy.loot(self.player)
            
            

            
            


class Event:
    def __init__(self,tyletype,player,getfacts):
        self.player = player
        self.facts = getfacts #0-realm,1-king,2-kingtitle
        self.stage = 1
        self.stillgoing = True
        self.battle = Battler(self.player)
        self.generator = namegenerator.Names()
        eventnumbers = [1,1,1,1,1,1,1,1,1,1,1,1,1] #Zuordnung siehe tyletypes.txt
        eventpicker = random.randrange(eventnumbers[tyletype])
        self.eventloc = [tyletype,eventpicker]

    def run(self):
        if self.eventloc[0] == 0:                  # Platzhalter
            if self.stage == 1:
                Tester = enemy.Enemy(3,"Tester")
                Tester.equipsword("Testschwert",2)
                self.battle.set(Tester,self.player)
                self.stage = 2
                return
            elif self.stage == 2:
                if self.battle.stillgoing:
                    self.battle.run()
                else:
                    self.stillgoing = False
        elif self.eventloc[0] == 1:                #Wasser
            if self.eventloc[1] == 0:
                print("Kampf (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 2:                #Wiese
            if self.eventloc[1] == 0:
                print("Kampf (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 3:                #Wald
            if self.eventloc[1] == 0:
                print("Kampf (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 4:                #Berge
            if self.eventloc[1] == 0:
                print("Kampf (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 5:                #Steppe
            if self.eventloc[1] == 0:
                print("Kampf (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 6:                #Dorf
            if self.eventloc[1] == 0:
                print("Kampf (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 7:                #Wüste
            if self.eventloc[1] == 0:
                print("Kampf (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 8:                #Hügel
            if self.eventloc[1] == 0:
                print("Kampf (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 9:                #Lavasee
            if self.eventloc[1] == 0:
                print("Kampf (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 10:                #Geröllebene
            if self.eventloc[1] == 0:
                print("Kampf (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 11:                #Friedhof
            if self.eventloc[1] == 0:
                print("Kampf (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 12:                #Burg
            if self.eventloc[1] == 0:
                print("Kampf (Platzhalter)")
                self.stillgoing = False
                input(">")
                return