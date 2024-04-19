import player
import random
import time
import items
import namegenerator

class Merchant:
    def __init__(self,player,strength,min = True, max = True):
        self.player = player
        self.strength = strength
        if min and self.strength < 3:
            self.strength = 3
        if max and self.strength > 20:
            self.strength = 20
        self.leave = False
        self.cost = random.randrange(4,8)
        self.offer = [0,0,0]
        self.prices = [0,0,0]
        self.soldout = [False,False,False]
        self.offertypes = [0,0,0] #0-Schwert, 1-Schild, 2-Dolch, 3-Axt, 4-Rüstung, 5-Schuhe, 6-Helm
        

    def shop(self):
        print("Angebote:")
        print("")
        index = 1
        for elements,prices,sold in zip(self.offer,self.prices,self.soldout):
            print(str(index))
            index += 1
            elements.printstats(0)
            if not sold:
                print("     " + str(prices) + " Gold")
            elif sold:
                print("Ausverkauft")
        print("4.  Shop verlassen")
        choice = input(">")
        if choice == "1":
            if not self.soldout[0]:
                self.buy(0)
            else:
                pass
        elif choice == "2":
            if not self.soldout[1]:
                self.buy(1)
            else:
                pass
        elif choice == "3":
            if not self.soldout[2]:
                self.buy(2)
            else:
                pass
        elif choice == "4":
            self.leave = True
        else:
            pass

    def buy(self,i):
        if self.prices[i] > self.player.gold:
            print("Nicht genug Gold...")
            time.sleep(2)
        elif self.offertypes[i] <= 3:
            self.player.equipweapon(self.offer[i],True)
            self.player.gold -= self.prices[i]
            self.soldout[i] = True
        elif self.offertypes[i] == 4:
            self.player.equiparmor(self.offer[i],True)
            self.player.gold -= self.prices[i]
            self.soldout[i] = True
        elif self.offertypes[i] == 5:
            self.player.equipshoes(self.offer[i],True)
            self.player.gold -= self.prices[i]
            self.soldout[i] = True
        elif self.offertypes[i] == 6:
            self.player.equiphelmet(self.offer[i],True)
            self.player.gold -= self.prices[i]
            self.soldout[i] = True

class Normal(Merchant):
    def __init__(self,player,strength):
        super().__init__(player,strength)
        for i in range(len(self.offer)):
            rand = random.randrange(-2,3)
            power = strength + rand
            if power <= 0:
                power = 1
            rare = random.randrange(4)
            types = [items.Sword(power,rare),items.Shield(power,rare),items.Dagger(power,rare),items.Axe(power,rare),items.Armor(power,rare),items.Shoes(power,rare),items.Helmet(power,rare)]
            randtype = random.randrange(len(types))
            self.offer[i] = types[randtype]
            self.offertypes[i] = randtype
            if rare == 0:
                self.prices[i] = int(round(self.cost / 2))
            else:
                self.prices[i] = self.cost * rare




class Event:
    def __init__(self,tyletype,player,getfacts):
        self.player = player
        self.facts = getfacts #0-realm,1-king,2-kingtitle
        self.stage = 1
        self.merch = 0
        self.stillgoing = True
        self.generator = namegenerator.Names()
        eventnumbers = [1,1,1,1,1,1,1,1,1,1,1,1,1] #Zuordnung siehe tyletypes.txt
        eventpicker = random.randrange(eventnumbers[tyletype])
        self.eventloc = [tyletype,eventpicker]

    def run(self):
        if self.eventloc[0] == 0:                        # Platzhalter
            print("Platzhalter")
            self.stillgoing = False
            return
        elif self.eventloc[0] == 1:                      # Wasser
            if self.eventloc[1] == 0:
                if self.stage == 1:
                    origin = self.generator.villagename()
                    print("Am Horizont nähert sich langsam ein Schiff""\n"
                          "und aufgrund der Entfernung lässt sich die""\n"
                          "Flagge nicht erkennen. Doch als es näher""\n"
                          "kommt, erkennst du die Farben der Handels-""\n"
                          "gilde von " + origin + ". Und wirklich: Bald schon""\n"
                          "hörst du das Rufen eines Mannes: 'Beste Waren!""\n"
                          "Direkt aus " + origin + "!'")
                    input(">")
                    if self.player.titlerep >= 2:
                        print("Ein nobel gekleideter Mann blickt von ""\n"
                              "der Reling. Als er dich erblickt, erschaudert""\n"
                              "er! Dein Ruf scheint bis nach " + origin + " vor-""\n"
                              "gedrungen zu sein. Nach einem kurzen Moment""\n"
                              "fängt sich der Mann gleich wieder und ruft:""\n"
                              + self.player.titlename + "!""\n"
                              "Welche Ehre! Vielleicht kann ich Sie von meiner""\n"
                              "Ware überzeugen.'")
                        input(">")
                        self.stage = 2
                        self.merch = Normal(self.player,self.player.lvl)
                    elif self.player.titlerep <= -2:
                        print("An Deck des Schiffs ist nun ein nobel gekleideter""\n"
                              "Mann zu sehen. Er scheint dich nun auch zu""\n"
                              "erkennen, denn seine Miene wird plötzlich finster.""\n"
                              "'Deine abscheulichen Taten sind in ganz " + self.facts[0] + "\n"
                              "bekannt. Solch Gesinde wird in " + origin + " nicht""\n"
                              "bedient! Zur Untermauerung seiner Worte bohrt""\n"
                              "sich ein Pfeil in eine Planke neben dir. Du""\n"
                              "erkennst die Ausweglosigkeit der Situation und""\n"
                              "gehst deines Weges.")
                        input(">")
                        self.stillgoing = False
                    else:
                        print("Auf dem Schiff gibt sich nobel gekleideter""\n"
                              "zu erkennen. Mit der Routine eines Geschäfts-""\n"
                              "mann und ohne eine Gefühlsregung erkennen""\n"
                              "zu lassen, präsentiert er seine Waren.")
                        input(">")
                        self.stage = 2
                        self.merch = Normal(self.player,self.player.lvl)
                if self.stage == 2:
                    if not self.merch.leave:
                        self.merch.shop()
                        self.player = self.merch.player
                    else:
                        self.stillgoing = False
                        pass
        elif self.eventloc[0] == 2:                #Wiese
            if self.eventloc[1] == 0:
                print("Händler (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 3:                #Wald
            if self.eventloc[1] == 0:
                print("Händler (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 4:                #Berge
            if self.eventloc[1] == 0:
                print("Händler (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 5:                #Steppe
            if self.eventloc[1] == 0:
                print("Händler (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 6:                #Dorf
            if self.eventloc[1] == 0:
                print("Händler (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 7:                #Wüste
            if self.eventloc[1] == 0:
                print("Händler (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 8:                #Hügel
            if self.eventloc[1] == 0:
                print("Händler (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 9:                #Lavasee
            if self.eventloc[1] == 0:
                print("Händler (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 10:                #Geröllebene
            if self.eventloc[1] == 0:
                print("Händler (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 11:                #Friedhof
            if self.eventloc[1] == 0:
                print("Händler (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 12:                #Burg
            if self.eventloc[1] == 0:
                print("Händler (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
                        