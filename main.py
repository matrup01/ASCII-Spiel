import os
import player
import map
import namegenerator
import colors
import event

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

player = player.Player()
map = map.Map(41,9)
generator = namegenerator.Names()
realm = generator.realmname()
king = generator.malepersonname()
kingtitle = generator.mtitles()
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
    print(player.titlename + " von " + realm + " (Lvl.: " + str(player.lvl) + "): ")
    print("HP: " + str(player.currenthp) + "/" + str(player.maxhp) + player.gethealthbar(3,28))
    print("XP: " + str(player.xp) + player.getxpbar(7,28))
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
        quit()
    else: 
        pass

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
            print("w,a,s,d  ...   Bewege dich über die Karte")
            print("j,n      ...   Beantworte Fragen mit ja/nein")
            print("q        ...   Beende das Spiel")
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
                        map.setvisited()
                elif move == "x":
                    print("10XP erhalten")
                    player.earnxp(10)
                    clear()
                else:
                    continue
        if battle:
            print("Kampf!!")
            move = input (">")
            if move == "m":
                battle =False
                overworld = True
            elif move == "q":
                exitgame()
            else:
                continue
        if merchant:
            print("Händler")
            move = input (">")
            if move == "m":
                merchant = False
                overworld = True
            elif move == "q":
                exitgame()
            else:
                continue
        if info:
            print("Heftige Hintergrundgeschichte (noch in Arbeit)")
            input(">")
            info = False
            overworld = True
            clear()
        if treasure:
            print("Schatz")
            move = input (">")
            if move == "m":
                treasure = False
                overworld = True
            elif move == "q":
                exitgame()
            else:
                continue
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
              
            

