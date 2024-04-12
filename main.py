import os
import player
import map
import namegenerator

run = True
menu = True
gamestart = False
firststage = False

player = player.Player()
map = map.Map(30,7)
generator = namegenerator.Names()
realm = generator.realmname()

def fullclear():
    os.system("cls")

def line(length):
    list = ["-" for i in range(length)]
    line = "O0"
    for element in list:
        line += element
    line += "0O"
    print(line)

def clear():
    os.system("cls")
    print(player.titlename + " von " + realm + ": ")
    print("HP: " + str(player.currenthp) + "/" + str(player.maxhp))
    map.printmap()
    
while run:
    while menu:
        fullclear()
        line(25)
        print(" |  1. Neues Spiel         |")
        print(" |  2. Wichtige Commands   |")
        print(" |  3. Lore                |")
        print(" |  4. Spiel beenden       |")
        line(25)

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

    while firststage:
        clear()
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
        else:
            continue