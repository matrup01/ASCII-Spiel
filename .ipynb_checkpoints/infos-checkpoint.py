import namegenerator
import player
import items
import random

class Event:
    def __init__(self,tyletype,player,getfacts):
        self.player = player
        self.facts = getfacts #0-realm,1-king,2-kingtitle
        self.stage = 1
        self.stillgoing = True
        self.generator = namegenerator.Names()
        eventnumbers = [1,1,1,1,1,1,1,1,1,1,1,1,1] #Zuordnung siehe tyletypes.txt
        eventpicker = random.randrange(eventnumbers[tyletype])
        self.eventloc = [tyletype,eventpicker]

    def run(self):
        if self.eventloc[0] == 0:                  # Platzhalter
            print("Platzhalter")
            self.stillgoing = False
            return
        elif self.eventloc[0] == 1:                #Wasser
            if self.eventloc[1] == 0:
                print("Info (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 2:                #Wiese
            if self.eventloc[1] == 0:
                print("Info (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 3:                #Wald
            if self.eventloc[1] == 0:
                print("Info (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 4:                #Berge
            if self.eventloc[1] == 0:
                print("Info (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 5:                #Steppe
            if self.eventloc[1] == 0:
                print("Info (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 6:                #Dorf
            if self.eventloc[1] == 0:
                print("Info (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 7:                #Wüste
            if self.eventloc[1] == 0:
                print("Info (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 8:                #Hügel
            if self.eventloc[1] == 0:
                print("Info (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 9:                #Lavasee
            if self.eventloc[1] == 0:
                print("Info (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 10:                #Geröllebene
            if self.eventloc[1] == 0:
                print("Info (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 11:                #Friedhof
            if self.eventloc[1] == 0:
                print("Info (Platzhalter)")
                self.stillgoing = False
                input(">")
                return
        elif self.eventloc[0] == 12:                #Burg
            if self.eventloc[1] == 0:
                print("Info (Platzhalter)")
                self.stillgoing = False
                input(">")
                return