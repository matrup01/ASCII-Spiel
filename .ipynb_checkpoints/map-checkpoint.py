import copy

class Map:
    def __init__(self,xlength,ylength):
        self.xlength = xlength
        self.ylength = ylength
        self.playerx = 0
        self.playery = 0
        self.mapdata = [["." for _ in range(self.xlength)] for _ in range(self.ylength)]

    def printmap(self):
        playerloc = copy.deepcopy(self.mapdata)
        playerloc[self.playery][self.playerx] = "x"

        list = ["=" for i in range(self.xlength)]
        tbline = "0O"
        for element in list:
            tbline += element
        tbline += "O0"
        print(tbline)
        for xarray in playerloc:
            line = " |"
            for xval in xarray:
                line += xval
            line += "|"
            print(line)
        print(tbline)
        restore = self.mapdata[self.playery][self.playerx]
        playerloc[self.playery][self.playerx] = restore

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
            
    