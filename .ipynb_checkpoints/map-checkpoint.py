import copy
import colors
import random

class Map:
    def __init__(self,xlength,ylength):
        self.colorer = colors.Colormap()
        self.xlength = xlength
        self.ylength = ylength
        self.playerx = 0
        self.playery = 0
        self.mapdata = [[[".",16,0,True] for _ in range(self.xlength)] for _ in range(self.ylength)] #Syntax: mapdata[y][x][0...symbol,1...color,2...tyletype,3...newcell]

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
        self.setvisited()

    def getstatus(self): #output: [x,y,tyletype,newcell,visitedcells]
        tyletype = self.mapdata[self.playery][self.playerx][2]
        newcell = self.mapdata[self.playery][self.playerx][3]
        vc = self.visitedcells()
        status = [self.playerx,self.playery,tyletype,newcell,vc]
        return status

    def setvisited(self):
        self.mapdata[self.playery][self.playerx][3] = False

    def visitedcells(self):
        n = 0
        for i in self.mapdata:
            for j in i:
                if not j[3]:
                    n += 1
        return n

    def generate(self): #tylelist-Syntax: [tyletype,Symbol,Farbe], Übersicht über Tyles in tyletypes.txt
        
        mainlist = [[2,"w",4],[5,".",7],[7,"S",6]]
        mainrand = random.randrange(len(mainlist))
        main = mainlist[mainrand]
        for xarray in self.mapdata:
            for tyle in xarray:
                tyle[0] = main[1]
                tyle[1] = main[2]
                tyle[3] = main[0]

        detaillist = [[1,"~",8],[3,"8",5],[4,"A",16],[6,"H",14],[8,"a",14],[9,"~",3],[10,"G",0]]
        counter = random.randrange(4,7)
        for i in range(counter):
            detailrand = random.randrange(len(detaillist))
            detail = detaillist[detailrand]
            detailx = random.randrange(7,14)
            detaily = random.randrange(5,6)
            xorigin = random.randrange(0,self.xlength-detailx)
            yorigin = random.randrange(0,self.ylength-detaily)
            for xarray in range(detaily):
                randval = random.randrange(-1,2)
                for tyle in range(detailx):
                    flavour = random.random()
                    xval = xorigin + tyle + randval
                    yval = yorigin + xarray
                    self.mapdata[yval][xval][0] = detail[1]
                    self.mapdata[yval][xval][1] = detail[2]
                    self.mapdata[yval][xval][3] = detail[0]

        detail2list = [[11,"t",1],[12,"B",15]]
        options = [True,False]
        checker = random.choice(options)
        if checker:
            detail2rand = random.randrange(len(detail2list))
            detail2 = detail2list[detail2rand]
            detail2x = random.randrange(7,14)
            detail2y = random.randrange(5,6)
            x2origin = random.randrange(0,self.xlength-detail2x)
            y2origin = random.randrange(0,self.ylength-detail2y)
            for xarray in range(detail2y):
                for tyle in range(detail2x):
                    xval = x2origin + tyle
                    yval = y2origin + xarray
                    self.mapdata[yval][xval][0] = detail2[1]
                    self.mapdata[yval][xval][1] = detail2[2]
                    self.mapdata[yval][xval][3] = detail2[0]
                            
            
    