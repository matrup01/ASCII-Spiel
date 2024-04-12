import copy
import colors

class Map:
    def __init__(self,xlength,ylength):
        self.colorer = colors.Colormap()
        self.xlength = xlength
        self.ylength = ylength
        self.playerx = 0
        self.playery = 0
        self.mapdata = [[[".",16] for _ in range(self.xlength)] for _ in range(self.ylength)] #Syntax: mapdata[y][x][0...symbol,1...color]

    def printmap(self):
        playerloc = copy.deepcopy(self.mapdata)
        playerloc[self.playery][self.playerx][0] = "x"
        playerloc[self.playery][self.playerx][1] = 3

        list = ["=" for i in range(self.xlength)]
        tbline = "0O"
        for element in list:
            tbline += element
        tbline += "O0"
        print(tbline)
        for xarray in playerloc:
            line = " |"
            for xval in xarray:
                tyle = self.colorer.returncolor(xval[0],xval[1])
                line += tyle
            line += "|"
            print(line)
        print(tbline)

    def playerup(self):
        if self.playery != 0:
            self.playery -= 1
        else:
            pass

    def playerdown(self):
        ymax = self.ylength - 1
        if self.playery != ymax:
            self.playery += 1
        else:
            pass

    def playerleft(self):
        if self.playerx != 0:
            self.playerx -= 1
        else:
            pass

    def playerright(self):
        xmax = self.xlength - 1
        if self.playerx != xmax:
            self.playerx += 1
        else:
            pass

    def playerset(self,x,y):
        self.playerx = x
        self.playery = y
            
    