import os
import player
import map
import namegenerator
import colors
import event
import blacksmiths
import items
import merchants
import loot
import battles
import infos

run = True
menu = True
gamestart = False
firststage = False
greetings = False
overworld = False
battle = False
merchant = False
info = False
treasure = False
boss = False
blacksmith = False

getfacts = [0,0,0] #0-realm,1-king,2-kingtitle
player = player.Player()
player.gold = 20   # für Testzwecke/später wieder entfernen (Gold wird direkt in der Klasse vergeben)
map = map.Map(41,9)
generator = namegenerator.Names()
realm = generator.realmname()
getfacts[0] = realm
king = generator.malepersonname()
getfacts[1] = king
kingtitle = generator.mtitles()
getfacts[2] = kingtitle
event = event.Event()
colorer = colors.Colormap()

def fullclear():
    os.system("cls")

def line(length,offset):
    line = ""
    offsetlist = [" " for i in range(offset)]
    for space in offsetlist:
       line += space 
    line += "O0"
    list = ["-" for i in range(length)]
    for element in list:
        line += element
    line += "0O"
    print(line)

def clear():
    os.system("cls")
    print("  " + player.titlename + " von " + realm + " (Lvl.: " + str(player.lvl) + "): ")
    print("  HP: " + str(player.currenthp) + "/" + str(player.maxhp) + player.gethealthbar(3,29))
    print("  XP: " + str(player.xp) + player.getxpbar(7,29))
    if player.gold < 10:
        offset1 = "   "
    elif player.gold < 100:
        offset1 = "  "
    elif player.gold < 1000:
        offset1 = " "
    else:
        offset1 = ""
    potions = colorer.returncolor("I",7) * player.potions
    rest = 22 - player.maxpotions
    offset2 = rest * " "
    print("  Gold: " + str(player.gold) + offset1 + "  Tränke:" + offset2 + potions)
    map.printmap()

def maketitle(): #ASCII-Art mit https://ascii.today/ erstellt
    print("  _  _____ _   _  ____ ____   ___  __  __ ____  ")
    print(" | |/ /_ _| \ | |/ ___|  _ \ / _ \|  \/  / ___| ")
    print(" | ' / | ||  \| | |  _| | | | | | | |\/| \___ \ ")
    print(" | . \ | || |\  | |_| | |_| | |_| | |  | |___) |")
    print(" |_|\_\___|_| \_|\____|____/ \___/|_|  |_|____/ ")
    print("  | \| | / _ \   |_   _||_ _||_   _|| |   | __| ")
    print("  | .` || (_) |    | |   | |   | |  | |__ | _|  ")
    print("  |_|\_| \___/     |_|  |___|  |_|  |____||___| ")
    print("")

def offsetprint(line,off):
    output = ""
    for i in range(off):
        output += " "
    output += line
    print(output)

def exitgame():
    print("Spiel verlassen?")
    confirm = input(">")
    confirm = confirm.capitalize()
    if confirm == "Ja" or confirm == "J" or confirm == "Y" or confirm == "Q":
        os.system("cls")
        quit()
    else: 
        pass

def options():
    print("w,a,s,d  ...   Bewege dich über die Karte")
    print("j,n      ...   Beantworte Fragen mit ja/nein")
    print("q        ...   Beende das Spiel")
    print("i        ...   Zeige das eigene Inventar")
    print("h        ...   Nutze einen Heiltrank")
    print("o        ...   Zeigt alle möglichen Befehle an")
    print("l        ...   Zeigt die Legende der Karte an")

def deathscreen():
    col = 3
    colorer.printcolor("       ___  _  _    ___  _ ____ ___ ",col)
    colorer.printcolor("       |  \ |  |    |__] | [__   |",col)
    colorer.printcolor("       |__/ |__|    |__] | ___]  |",col)
    colorer.printcolor("____ ____ ____ ___ ____ ____ ___  ____ _  _ ",col)
    colorer.printcolor("| __ |___ [__   |  |  | |__/ |__] |___ |\ | ",col)
    colorer.printcolor("|__] |___ ___]  |  |__| |  \ |__] |___ | \|",col)
    input()
    input("Zum Beenden Taste drücken")
    os.system("cls")
    quit()

while run:
    while menu:
        fullclear()
        maketitle()
        line(25,10)
        offsetprint("|  1. Neues Spiel         |",11)
        offsetprint("|  2. Wichtige Commands   |",11)
        offsetprint("|  3. Lore                |",11)
        offsetprint("|  4. Spiel beenden       |",11)
        line(25,10)

        choice = input(">")
        if choice == "1":
            menu = False
            gamestart = True
        elif choice == "2":
            fullclear()
            print("Befehle in der Overworld:")
            print("")
            options()
            print("")
            print("WICHTIG -- Alle Befehle müssen mit Enter bestätigt werden!")
            input(">")
        elif choice == "3":
            fullclear()
            print("Eine spannende Gutenachtgeschichte (noch in Entwicklung)")
            input(">")
        elif choice == "4":
            quit()
        else:
            continue

    while gamestart:
        fullclear()
        print("Gib deinen Namen ein")
        nameask = input(">")
        player.setname(str(nameask))
        gendersetup = True
        while gendersetup:
            print("Bist du eine Frau oder ein Mann?")
            genderask = input("m/w  >")
            genderask = genderask.capitalize()
            if genderask == "M" or genderask == "W" or genderask == "F":
                player.setgender(genderask)
                gendersetup = False
        gamestart = False
        firststage = True
        greetings = True
        overworld = True
        map.playerset(20,8)
        map.generate()
        clear()

    while firststage:
        if overworld:
            if greetings:
                move = input("Willkommen im Königreich " + realm + ", in dem König " + king + " " + kingtitle + " herrscht! >")
                greetings = False
            else:
                move = input(">")
                if move == "q":
                    exitgame()
                    clear()
                elif move == "w" or move == "a" or move == "s" or move == "d":
                    if move == "w":
                        map.playerup()
                    elif move == "a":
                        map.playerleft()
                    elif move == "s":
                        map.playerdown()
                    elif move == "d":
                        map.playerright()
                    clear()
                    if map.getstatus()[3]:
                        eventpicker = event.select(map.getstatus())
                        overworld = False
                        if eventpicker == 0:
                            battle = True
                        elif eventpicker == 1:
                            merchant = True
                        elif eventpicker == 2:
                            info = True
                        elif eventpicker == 3:
                            treasure = True
                        elif eventpicker == 4:
                            boss = True
                        elif eventpicker == 5:
                            blacksmith = True
                        map.setvisited()
                        clear()
                elif move == "i":
                    player.printequip()
                    input(">")
                    clear()
                elif move == "h":
                    if player.potions > 0:
                        player.currenthp = player.maxhp
                        player.potions -= 1
                    else: 
                        pass
                    clear()
                elif move == "o":
                    options()
                elif move == "l":
                    print("Legende:")
                    print("")
                    first = colorer.returncolor("x",3)
                    print(first + "   ...   " + player.titlename + " von " + realm)
                    map.printlegend()
                    input(">")
                    clear()
                elif move == "debug":
                    tt = input("tyletype?")
                    map.testevents(tt)
                    clear()
                else:
                    continue
        if battle:
            bevent = battles.Event(map.getstatus()[2],player,getfacts)
            while bevent.stillgoing:
                bevent.run()
                player = bevent.player
                if not bevent.battle.noclear:
                    clear()
                if player.currenthp <= 0:
                    deathscreen()
                battle = False
                overworld = True
        if merchant:
            mevent = merchants.Event(map.getstatus()[2],player,getfacts)
            while mevent.stillgoing:
                mevent.run()
                player = mevent.player
                clear()
                if player.currenthp <= 0:
                    deathscreen()
            merchant = False
            overworld = True
        if blacksmith:
            bsevent = blacksmiths.Event(map.getstatus()[2],player,getfacts)
            while bsevent.stillgoing:
                bsevent.run()
                player = bsevent.player
                clear()
                if player.currenthp <= 0:
                    deathscreen()
            blacksmith = False
            overworld = True
        if info:
            ievent = infos.Event(map.getstatus()[2],player,getfacts)
            while ievent.stillgoing:
                ievent.run()
                player = ievent.player
                clear()
                if player.currenthp <= 0:
                    deathscreen()
                info = False
                overworld = True
        if treasure:
            looter = loot.Event(map.getstatus()[2],player,getfacts)
            while looter.stillgoing:
                looter.run()
                player = looter.player
                clear()
                if player.currenthp <= 0:
                    deathscreen()
            treasure = False
            overworld = True
        if boss:
            colorer.printcolor("Boss",3)
            move = input (">")
            if move == "m":
                boss = False
                overworld = True
            elif move == "q":
                exitgame()
            else:
                continue
              
            

