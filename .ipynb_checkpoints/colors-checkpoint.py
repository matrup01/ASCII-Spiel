import numpy as np

class Colorpallet:
    def __init__(self): 
        self.colors = np.array([[0,30],[1,30],[0,31],[1,31],[0,32],[1,32],[0,33],[1,33],[0,34],[1,34],[0,35],[1,35],[0,36],[1,36],[0,37],[1,37],[0,0]])
        #0 --> grau
        #1 --> dunkelgrau
        #2 --> hellrot
        #3 --> rot
        #4 --> hellgrün
        #5 --> grün
        #6 --> gelb
        #7 --> braun
        #8 --> hellblau
        #9 --> blau
        #10 --> pink
        #11 --> violett
        #12 --> helles cyan
        #13 --> cyan
        #14 --> hellgrau
        #15 --> light blueish gray
        #16 --> weiß/standard
    
    def printcolor(self,line,col):
        if col == 16:
            print(line)
        elif col < len(self.colors):
            output = "\033[" + str(self.colors[col][0]) + ";" + str(self.colors[col][1]) + "m"
            output += line
            output += "\033[0m"
            print(output)
        else:
            print(line)

    def returncolor(self,line,col):
        if col == 16:
            return line
        elif col < len(self.colors):
            output = "\033[" + str(self.colors[col][0]) + ";" + str(self.colors[col][1]) + "m"
            output += line
            output += "\033[0m"
            return output
        else:
            return line
    
        