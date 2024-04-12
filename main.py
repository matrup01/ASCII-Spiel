import os
import player
import map
import namegenerator
import colors

run = True
menu = True
gamestart = False
firststage = False
greetings = False
battle = False

player = player.Player()
map = map.Map(31,7)
generator = namegenerator.Names()
realm = generator.realmname()

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
    print(player.titlename + " von " + realm + ": ")
    print("HP: " + str(player.currenthp) + "/" + str(player.maxhp))
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
        gamestart = False
        firststage = True
        greetings = True
        map.playerset(15,6)

    while firststage:
        clear()
        if not battle:
            if greetings:
                move = input("Willkommen im Königreich " + realm + "! >")
                greetings = False
            else:
                move = input(">")
                if move == "w":
                    map.playerup()
                    clear()
                elif move == "a":
                    map.playerleft()
                    clear()
                elif move == "s":
                    map.playerdown()
                    clear()
                elif move == "d":
                    map.playerright()
                    clear()
                elif move == "q":
                    print("Spiel verlassen?")
                    confirm = input(">")
                    confirm = confirm.capitalize()
                    if confirm == "Ja" or confirm == "J":
                        quit()
                elif move == "b":
                        battle = True
                else:
                    continue
        if battle:
            print("Kampf!!")
            move = input (">")
            if move == "m":
                battle = False
            elif move == "q":
                print("Spiel verlassen?")
                confirm = input(">")
                confirm = confirm.capitalize()
                if confirm == "Ja" or confirm == "J":
                    quit()
            else:
                continue

