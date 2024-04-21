import random
import namegenerator
import player
import enemy
import items
import colors
import numpy as np

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
        if loot:
            self.loot = True
        else:
            self.loot = False

    def battleheader(self):
        p = self.player.titlename + ": "
        if self.playerstats[3] != 0:
            p += self.colorer.returncolor("G" + str(int(round(self.playerstats[3],0))) + " ",4)
        if self.playerstats[4] != 0:
            p += self.colorer.returncolor("F" + str(int(round(self.playerstats[4],0))) + " ",2)
        if self.playerstats[5] != 0:
            p += self.colorer.returncolor("B" + str(int(round(self.playerstats[5],0))) + " ",3)
        if self.playerstats[6] != 0:
            prozent = int(round(self.playerstats[6] * 100),0)
            p += self.colorer.returncolor("R" + str(prozent) + "% ",13)
        if self.playerstats[7] != 0:
            p += self.colorer.returncolor("D" + str(self.playerstats[7]) + " ",11)
        if self.playerstats[8] != 0:
            p += self.colorer.returncolor("B" + str(self.playerstats[8]) + " ",14)
        if self.playerstats[10] != 0:
            prozent  = int(round(self.playerstats[10] * 100),0)
            p += self.colorer.returncolor("L" + st(prozent) + " ",3)
        print(p)
        print(str(int(round(self.player.currenthp,0))) + "/" + str(self.player.maxhp) + self.player.gethealthbar(3,30))
        e = self.enemy.name + ": "
        if self.enemystats[3] != 0:
            e += self.colorer.returncolor("G" + str(int(round(self.enemystats[3],0))) + " ",4)
        if self.enemystats[4] != 0:
            e += self.colorer.returncolor("F" + str(int(round(self.enemystats[4],0))) + " ",2)
        if self.enemystats[5] != 0:
            e += self.colorer.returncolor("B" + str(int(round(self.enemystats[5],0))) + " ",3)
        if self.enemystats[6] != 0:
            prozent = int(round(self.enemystats[6] * 100),0)
            e += self.colorer.returncolor("R" + str(prozent) + "% ",13)
        if self.enemystats[7] != 0:
            e += self.colorer.returncolor("D" + str(self.enemystats[7]) + " ",11)
        if self.enemystats[8] != 0:
            e += self.colorer.returncolor("B" + str(self.enemystats[8]) + " ",14)
        if self.enemystats[10] != 0:
            prozent  = int(round(self.enemystats[10] * 100),0)
            e += self.colorer.returncolor("L" + st(prozent) + " ",3)
        print(e)
        print(str(int(round(self.enemy.currenthp,0))) + "/" + str(self.enemy.maxhp) + self.enemy.gethealthbar(3,30))

    def run(self):
        if self.phase == 0:
            self.turn()
            if self.enemy.currenthp <= 0:
                self.phase = 2
                return
            else:
                self.phase = 0
                return
        elif self.phase == 2:
            self.end()
            self.noclear = False
            self.stillgoing = False

    def end(self):
        print("Du hast " + self.enemy.name + " besiegt, du erhältst " + str(self.enemy.xp) + "XP")
        self.player.earnxp(self.enemy.xp)
        rand = random.randrange(2)
        if rand == 1:
            if self.loot:
                self.enemy.loot(self.player)
        input(">")

    def turn(self):
        self.battleheader()
        options = input("Wie gehst du vor? >")
        if options == "o":
            print("o        ...   Zeigt alle möglichen Befehle an")
            print("i        ...   Zeigt das eigene Inventar an")
            print("e        ...   Zeigt Informationen über den Gegner an")
            print("h        ...   Verwende einen Heiltrank")
            print("l        ...   Nutze die Waffe in der linken Hand")
            print("r        ...   Nutze die Waffe in der rechten Hand")
            print("f        ...   Versuche zu flüchten")
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
        elif options == "l" or options == "r" or options == "h" or options == "f":
            self.realturn(options)

    def realturn(self,options):
        turncalc = np.array([np.zeros(12),np.zeros(12)]) # [0...player,1...enemy][0...damage,1...block,2...verfehlt(1 für ja),3-10...wie items,11...off/def/h/f]
        playerweapon = ""
        enemyweapon = ""
        turncalc[0][1] = self.player.armor.defense + self.player.helmet.defense
        turncalc[1][1] = self.enemy.armor.defense + self.enemy.helmet.defense + self.enemy.stats[1]
        if options == "l":
            if self.player.haslweapon:
                playerweapon = self.player.lweapon.name
                if self.player.lweapon.type == "off":
                    turncalc[0][11] = 0
                    evs = (1 - self.player.lweapon.stats[2]) + (1 - self.player.lweapon.stats[2]) * (self.enemy.helmet.evasiveness + self.enemy.evasiveness)
                    if random.random() >= evs:
                        turncalc[0][0] = self.player.lweapon.stats[0] + self.enemystats[5]
                        turncalc[1][3] = self.player.lweapon.stats[3]
                        turncalc[1][4] = self.player.lweapon.stats[4]
                        turncalc[1][5] = self.player.lweapon.stats[5]
                        turncalc[1][8] = self.player.lweapon.stats[8]
                        turncalc[0][10] = self.player.lweapon.stats[10]
                    else:
                        turncalc[0][2] = 1
                        turncalc[0][0] = 0
                elif self.player.lweapon.type == "def":
                    turncalc[0][11] = 1
                    turncalc[0][1] += self.player.lweapon.stats[1]
                    turncalc[0][6] = self.player.lweapon.stats[6]
                    turncalc[0][7] = self.player.lweapon.stats[7]
            else:
                return
        elif options == "r":
            if self.player.hasrweapon:
                playerweapon = self.player.rweapon.name
                if self.player.rweapon.type == "off":
                    turncalc[0][11] = 0
                    evs = (1 - self.player.rweapon.stats[2]) + (1 - self.player.rweapon.stats[2]) * (self.enemy.helmet.evasiveness + self.enemy.evasiveness)
                    if random.random() >= evs:
                        turncalc[0][0] = self.player.rweapon.stats[0] + self.enemystats[5]
                        turncalc[1][3] = self.player.rweapon.stats[3]
                        turncalc[1][4] = self.player.rweapon.stats[4]
                        turncalc[1][5] = self.player.rweapon.stats[5]
                        turncalc[1][8] = self.player.rweapon.stats[8]
                        turncalc[0][10] = self.player.rweapon.stats[10]
                    else:
                        turncalc[0][2] = 1
                        turncalc[0][0] = 0
                elif self.player.rweapon.type == "def":
                    turncalc[0][11] = 1
                    turncalc[0][1] += self.player.rweapon.stats[1]
                    turncalc[0][6] = self.player.rweapon.stats[6]
                    turncalc[0][7] = self.player.rweapon.stats[7]
            else:
                return
        elif options == "h":
            if self.player.potions > 0:
                self.player.currenthp = self.player.maxhp
                self.player.potions -= 1
                turncalc[0][11] = 2
            else: 
                return
        elif options == "f":
            turncalc[0][11] = 3
        if self.enemy.haslweapon and self.enemy.hasrweapon:
            choice = random.randrange(2)
        elif self.enemy.haslweapon and not self.enemy.hasrweapon:
            choice = 0
        elif self.enemy.hasrweapon and not self.enemy.haslweapon:
            choice = 1
        if choice == 0:
            enemyweapon = self.enemy.lweapon.name
            if self.enemy.lweapon.type == "off":
                turncalc[1][11] = 0
                evs = (1 - self.enemy.lweapon.stats[2]) + (1 - self.enemy.lweapon.stats[2]) * self.player.helmet.evasiveness
                if random.random() >= evs:
                    turncalc[1][0] = self.enemy.lweapon.stats[0] + self.enemy.stats[0] + self.playerstats[5]
                    turncalc[0][3] = self.enemy.lweapon.stats[3] + self.enemy.stats[3]
                    turncalc[0][4] = self.enemy.lweapon.stats[4] + self.enemy.stats[4]
                    turncalc[0][5] = self.enemy.lweapon.stats[5] + self.enemy.stats[5]
                    turncalc[0][8] = self.enemy.lweapon.stats[8] + self.enemy.stats[8]
                    turncalc[1][10] = self.enemy.lweapon.stats[10] + self.enemy.stats[10]
                else:
                    turncalc[1][2] = 1
                    turncalc[1][0] = 0
            elif self.enemy.lweapon.type == "def":
                turncalc[1][11] = 1
                turncalc[1][1] += self.enemy.lweapon.stats[1]
                turncalc[1][6] = self.enemy.lweapon.stats[6] + self.enemy.stats[6]
                turncalc[1][7] = self.enemy.lweapon.stats[7] + self.enemy.stats[7]
        elif choice == 1:
            enemyweapon = self.enemy.rweapon.name
            if self.enemy.rweapon.type == "off":
                turncalc[1][11] = 0
                evs = (1 - self.enemy.rweapon.stats[2]) + (1 - self.enemy.rweapon.stats[2]) * self.player.helmet.evasiveness
                if random.random() >= evs:
                    turncalc[1][0] = self.enemy.rweapon.stats[0] + self.enemy.stats[0] + self.playerstats[5]
                    turncalc[0][3] = self.enemy.rweapon.stats[3] + self.enemy.stats[3]
                    turncalc[0][4] = self.enemy.rweapon.stats[4] + self.enemy.stats[4]
                    turncalc[0][5] = self.enemy.rweapon.stats[5] + self.enemy.stats[5]
                    turncalc[0][8] = self.enemy.rweapon.stats[8] + self.enemy.stats[8]
                    turncalc[1][10] = self.enemy.rweapon.stats[10] + self.enemy.stats[10]
                else:
                    turncalc[1][2] = 1
                    turncalc[1][0] = 0
            elif self.enemy.rweapon.type == "def":
                turncalc[1][11] = 1
                turncalc[1][1] += self.enemy.rweapon.stats[1]
                turncalc[1][6] = self.enemy.rweapon.stats[6] + self.enemy.stats[6]
                turncalc[1][7] = self.enemy.rweapon.stats[7] + self.enemy.stats[7]
        if turncalc[0][11] == 0 and turncalc[1][11] == 0:
            self.calculateaa(turncalc,playerweapon,enemyweapon)
        elif turncalc[0][11] == 0 and turncalc[1][11] == 1:
            self.calculatead(turncalc,playerweapon,enemyweapon)
        elif turncalc[0][11] != 0 and turncalc[1][11] == 0:
            self.calculateda(turncalc,playerweapon,enemyweapon)
        elif turncalc[0][11] != 0 and turncalc[1][11] == 1:
            self.calculatedd(turncalc,playerweapon,enemyweapon)
        for debuff in [3,4]:
            if self.playerstats[debuff] > 0:
                self.player.currenthp -= self.playerstats[debuff]
                print("Die " + self.debuffname(debuff) + " schadet dir (" + str(self.playerstats[debuff]) + ")")
            if self.enemystats[debuff] > 0:
                self.enemy.currenthp -= self.enemystats[debuff]
                print("Die " + self.debuffname(debuff) + " schadet " + self.enemy.name + " (" + str(self.enemystats[debuff]) + ")")
        if self.enemy.currenthp < 0:
            self.enemy.currenthp = 0
        self.battleheader()
        for debuff in [3,4,5]:
            if self.playerstats[debuff] > 0:
                self.playerstats[debuff] -= 1
            if self.enemystats[debuff] > 0:
                self.enemystats[debuff] -= 1
        input(">")

    def calculateaa(self,turncalc,playerweapon,enemyweapon):
        enemystun = False
        enemymissed = False
        if turncalc[1][2] == 0:
            if turncalc[1][8] <= random.random():
                print(self.enemy.name + " greift dich mit " + enemyweapon)
                print("an und fügt dir " + str(turncalc[1][0]) + " Schaden zu, wobei du " + str(turncalc[0][1]) + " davon abwehren kannst")
                damage = turncalc[1][0] - turncalc[0][1]
                if damage < 0:
                    damage = 0
                self.player.currenthp -= damage
                if turncalc[1][10] > 0:
                    ls = round(damage * turncalc[1][10],0)
                    self.enemy.currenthp += ls
                    print(self.enemy.name + " heilt sich durch den Angriff. (" + str(int(ls)) + ")")
                self.checkdebuffs(turncalc,0)
            else:
                enemystun = True
        else:
            print(self.enemy.name + " greift dich mit " + enemyweapon)
            print("an, doch sein Angriff verfehlt dich.")
            enemymissed = True
        if turncalc[0][2] == 0 or enemystun:
            if enemystun or turncalc[0][8] <= random.random() or enemymissed:
                print("Du fügst " + self.enemy.name)
                print(str(turncalc[0][0]) + " Schaden zu, wobei " + str(turncalc[1][1]) + " davon abgeblockt werden")
                damage = turncalc[0][0] - turncalc[1][1]
                if damage < 0:
                    damage = 0
                self.enemy.currenthp -= damage
                if turncalc[0][10] > 0:
                    ls = round(damage * turncalc[0][10],0)
                    self.player.currenthp += ls
                    print("Du heilst dich durch den Angriff. (" + str(int(ls)) + ")")
            else:
                print("Du wurdest durch den Angriff von " + self.enemy.name + " betäubt.")
            if enemystun:
                print("Dein Angriff hat " + self.enemy.name + " betäubt")
            self.checkdebuffs(turncalc,1)
        else:
            print("Dein Angriff verfehlt sein Ziel!")

    def calculatead(self,turncalc,playerweapon,enemyweapon):
        print(self.enemy.name + " geht hinter seinem " + enemyweapon + " in Deckung.")
        if turncalc[0][2] == 0:
            print("Du fügst " + self.enemy.name)
            print(str(turncalc[0][0]) + " Schaden zu, wobei " + str(turncalc[1][1]) + " davon abgeblockt werden")
            damage = turncalc[0][0] - turncalc[1][1]
            if damage < 0:
                damage = 0
            self.enemy.currenthp -= damage
            if turncalc[0][10] > 0:
                    ls = round(damage * turncalc[0][10],0)
                    self.player.currenthp += ls
                    print("Du heilst dich durch den Angriff. (" + str(int(ls)) + ")")
            if turncalc[1][6] > 0:
                reflect = round(damage * turncalc[1][6],0)
                self.player.currenthp -= reflect
                print(self.colorer.returncolor(str(int(reflect)) + " Schadenspunkte",13) + " werden auf dich zurückgeworfen")
            if turncalc[1][7] > 0:
                self.player.currenthp -= turncalc[1][7]
                print("Du verletzt dich an den " + self.colorer.returncolor("Dornen (" + str(turncalc[1][7]) + ")",11))
            self.checkdebuffs(turncalc,1)

        else:
            print("Dein Angriff verfehlt sein Ziel!")

    def calculateda(self,turncalc,playerweapon,enemyweapon):
        if turncalc[0][11] == 1:
            print("Du gehst hint deinem " + playerweapon + " in Deckung.")
        elif turncalc[0][11] == 2:
            print("Du frischst deine HP mit einem Heiltrank auf.")
        elif turncalc[0][11] == 3:
            checker = 0.5
            if self.player.hasshoes:
                checker += self.player.shoes.speed
            if random.random() <= checker:
                print("Dir gelingt die Flucht!")
                self.stillgoing = False
                return
            else:
                print("Flucht gescheitert!")
        if turncalc[1][2] == 0:
            print(self.enemy.name + " greift dich mit " + enemyweapon)
            print("an und fügt dir " + str(turncalc[1][0]) + " Schaden zu, wobei du " + str(turncalc[0][1]) + " davon abwehren kannst")
            damage = turncalc[1][0] - turncalc[0][1]
            if damage < 0:
                damage = 0
            self.enemy.currenthp -= damage
            if turncalc[1][10] > 0:
                    ls = round(damage * turncalc[1][10],0)
                    self.enemy.currenthp += ls
                    print(self.enemy.name + " heilt sich durch den Angriff. (" + str(int(ls)) + ")")
            if turncalc[0][6] > 0:
                reflect = round(damage * turncalc[0][6],0)
                self.enemy.currenthp -= reflect
                print(self.colorer.returncolor(str(int(reflect)) + " Schadenspunkte",13) + " werden auf " + self.enemy.name + " zurückgeworfen")
            if turncalc[0][7] > 0:
                self.enemy.currenthp -= turncalc[0][7]
                print(self.enemy.name + " verletzt sich an den " + self.colorer.returncolor("Dornen (" + str(turncalc[0][7]) + ")",11))
            self.checkdebuffs(turncalc,0)
        else:
            print(self.enemy.name + " greift dich mit " + enemyweapon)
            print("an, doch sein Angriff verfehlt dich.")

    def calculatedd(self,turncalc,playerweapon,enemyweapon):
        if turncalc[0][11] == 1:
            print("Ihr geht beide in die Defensive und wartet auf einen günstigeren Moment")
        elif turncalc[0][11] == 2:
            print("Du frischst deine HP mit einem Heiltrank auf.")
            print(self.enemy.name + " geht hinter seinem " + enemyweapon + " in Deckung.")
        elif turncalc[0][11] == 3:
            checker = 0.5
            if self.player.hasshoes:
                checker += self.player.shoes.speed
            if random.random() <= checker:
                print("Dir gelingt die Flucht!")
                self.stillgoing = False
                return
            else:
                print("Flucht gescheitert!")
                print(self.enemy.name + " geht hinter seinem " + enemyweapon + " in Deckung.")

    def checkdebuffs(self,turncalc,recipient):
        for debuff in [3,4,5]:
            debuffer = turncalc[recipient][debuff]
            if recipient == 0:
                if debuffer > 0:
                    print("Dir wurden " + self.colorer.returncolor(str(debuffer) + " " + self.debuffname(debuff),self.debuffcolor(debuff)) + " zugefügt.")
                    self.playerstats[debuff] += debuffer
            elif recipient == 1:
                if debuffer > 0:
                    print("Du hast " + self.enemy.name + " " + self.colorer.returncolor(str(debuffer) + " " + self.debuffname(debuff),self.debuffcolor(debuff)) + " zugefügt.")
                    self.enemystats[debuff] += debuffer

    def debuffname(self,n):
        if n == 3:
            return "Vergiftung"
        elif n == 4:
            return "Verbrennung"
        elif n == 5:
            return "Blutung"
        else:
            return ""

    def debuffcolor(self,n):
        if n == 3:
            return 4
        elif n == 4:
            return 2
        elif n == 5:
            return 3
        else:
            return 16
            

            
        
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
                Tester.equipsword("Testschwert",2,lifesteal=0.5)
                Tester.equipshield("Testschild",1)
                self.battle.set(Tester,self.player)
                self.stage = 2
                print("Du wirst von " + Tester.name + " angegriffen!")
                input()
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