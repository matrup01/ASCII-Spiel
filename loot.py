import player
import items
import namegenerator
import random
import colors

class Event:
    def __init__(self,tyletype,player,getfacts):
        self.player = player
        self.facts = getfacts #0-realm,1-king,2-kingtitle
        self.stage = 1
        self.power = self.player.lvl
        self.stillgoing = True
        self.colorer = colors.Colormap()
        self.generator = namegenerator.Names()
        eventnumbers = [1,1,1,1,1,1,1,1,1,1,1,1,1] #Zuordnung siehe tyletypes.txt
        eventpicker = random.randrange(eventnumbers[tyletype])
        self.eventloc = [tyletype,eventpicker]

    def run(self):
        if self.eventloc[0] == 0:                 #Platzhalter
            print("Schatz (Platzhalter)")
            self.stillgoing = False
            return
        elif self.eventloc[0] == 1:               #Wasser
            if self.eventloc[1] == 0:
                if self.stage == 1:
                    print("In einiger Entfernung taucht ein Schiff auf. Als""\n"
                          "es näher kommt, erkennst du zerfetzte Segel und""\n"
                          "einen morschen Rumpf. Es handelt sich um ein""\n"
                          "Geisterschiff. Möchtest du an Bord gehen und es""\n"
                          "untersuchen?")
                    choice = input("j/n >")
                    if choice == "j":
                        option = random.randrange(3)
                        if option == 0:
                            self.stage = 2
                        elif option == 1:
                            self.stage = 3
                        elif option == 2:
                            self.stage = 4
                    elif choice == "n":
                        self.stillgoing = False
                        return
                    else:
                        return
                elif self.stage == 2:
                    print("Auf dem Schiff dürfte vor langer Zeit ein Kampf""\n"
                          "getobt haben. Überall liegen Skelette in""\n"
                          "rostigen Rüstungen. In den Überresten eines""\n"
                          "Raumes, bei dem es sich einmal um die Kapitäns-""\n"
                          "kajüte gehandelt haben dürfte findest du eine""\n"
                          "Kiste. Das rostige Schloss gibt sofort nach und""\n"
                          "du findest ein Schwert!")
                    input(">")
                    loot = items.Sword(self.power,2)
                    loot.name = self.colorer.returncolor("Schwert des Kapitäns",9)
                    self.player.equipweapon(loot)
                    self.stillgoing = False
                    return
                elif self.stage == 3:
                    print("Du gehst an Bord des Schiffs und erblickst zahl-""\n"
                          "reiche Leichen von Händlern. Vermutlich sind sie""\n"
                          "einem Piratenangriff zum Opfer gefallen. Bei der""\n"
                          "Untersuchung des Schiffs erhärtet sich dieser Ver-""\n"
                          "dacht, denn sämtliche Waren wurden geplündert. Da es""\n"
                          "auf dem Schiff nichts mehr zu holen gibt, gehst du""\n"
                          "von Bord.")
                    input(">")
                    self.stillgoing = False
                    return
                elif self.stage == 4:
                    print("An Bord des Schiffes hörst du es knarren und""\n"
                          "knacksen. Du ignorierst dein mulmiges Gefühl""\n"
                          "und suchst weiter nach Schätzen. Doch dein Mut""\n"
                          "wird nicht belohnt. Gerade als du einen viel-""\n"
                          "versprechenden Raum betrittst, gibt das Holz""\n"
                          "unter dir nach und du stürtzt in den Bauch des""\n"
                          "Schiffs. (" + self.colorer.returncolor("- 2HP",3) + ") Durch deinen Aufprall wird""\n"
                          "die Struktur des Schiffs geschädigt und Wasser""\n"
                          "dringt ein. Du kannst es gerade noch rechtzeitig""\n"
                          "verlassen, bevor es untergeht.")
                    input(">")
                    self.stage = 5
                elif self.stage == 5:
                    self.stillgoing = False
                    self.player.currenthp -=15
                    self.stillgoing = False
                    return
        elif self.eventloc[0] == 2:                #Wiese
            if self.eventloc[1] == 0:
                print("Schatz (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 3:                #Wald
            if self.eventloc[1] == 0:
                print("Schatz (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 4:                #Berge
            if self.eventloc[1] == 0:
                print("Schatz (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 5:                #Steppe
            if self.eventloc[1] == 0:
                print("Schatz (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 6:                #Dorf
            if self.eventloc[1] == 0:
                print("Schatz (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 7:                #Wüste
            if self.eventloc[1] == 0:
                print("Schatz (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 8:                #Hügel
            if self.eventloc[1] == 0:
                print("Schatz (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 9:                #Lavasee
            if self.eventloc[1] == 0:
                print("Schatz (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 10:                #Geröllebene
            if self.eventloc[1] == 0:
                print("Schatz (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 11:                #Friedhof
            if self.eventloc[1] == 0:
                print("Schatz (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 12:                #Burg
            if self.eventloc[1] == 0:
                print("Schatz (Platzhalter)")
                self.stillgoing = False
                input(">")
                return