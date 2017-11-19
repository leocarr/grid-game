from graphics import *
import random
import math

win = GraphWin("Grid Game", 400, 400)

shape = "square"
cells = []
CELLSIZE = 50
gameOver = False
cols = int(win.getHeight()/CELLSIZE)-2
rows = int(win.getWidth()/CELLSIZE)-2
adjacent = [2,3,0,1]


class Cell:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.lines = [0,0,0,0]
        self.owner = ""

    def setLine(self,l):
        self.lines[l] = 1
        if(sum(self.lines) == 4):
            self.setOwner(player)
            
    def getLine(self,l):
        if self.lines[l] == 1:
            return True
        else:
            return False

    def setOwner(self,p):
        rec = Rectangle(Point(x*CELLSIZE,y*CELLSIZE),Point((x+1)*CELLSIZE,(y+1)*CELLSIZE))
        rec.setFill(p)
        rec.draw(win)
        

for i in range(1,int(win.getHeight()/CELLSIZE)):
    for j in range(1,int(win.getWidth()/CELLSIZE)-1):       
        p = Point(i*CELLSIZE,j*CELLSIZE)
        p.draw(win)
        if i < int(win.getHeight()/CELLSIZE)-1:
            cell = Cell(i,j)
            cells.append(cell)
    p = Point(i*CELLSIZE,int(win.getWidth()-CELLSIZE))
    p.draw(win)

player = "blue"

def getAdjInd(x,y,l):
    i = (y-1)*rows + (x-1)
    if l == 0 and y > 1:
        i -= rows
    elif l == 2 and y < rows:
        i += rows
    elif l == 1 and x > 1:
        i -= 1
    elif x < cols:
        i += 1
    return i
    
    

while gameOver == False:
    turn = win.getMouse()
    x = int(turn.getX()/CELLSIZE)
    y = int(turn.getY()/CELLSIZE)
    line = -1
    l = Line(Point(x*CELLSIZE,y*CELLSIZE),Point((x+1)*CELLSIZE,y*CELLSIZE))
    if turn.getX()%CELLSIZE < CELLSIZE/5:
        line = 1 #left
        l = Line(Point((x)*CELLSIZE,y*CELLSIZE),Point((x)*CELLSIZE,(y+1)*CELLSIZE))
    elif turn.getX()%CELLSIZE > CELLSIZE*4/5:
        line = 3 #right
        l = Line(Point((x+1)*CELLSIZE,y*CELLSIZE),Point((x+1)*CELLSIZE,(y+1)*CELLSIZE))
    elif turn.getY()%CELLSIZE < CELLSIZE/5:
        line = 0 #top
        l = Line(Point(x*CELLSIZE,y*CELLSIZE),Point((x+1)*CELLSIZE,y*CELLSIZE))
    elif turn.getY()%CELLSIZE > CELLSIZE*4/5:
        line = 2 #bottom
        l = Line(Point(x*CELLSIZE,(y+1)*CELLSIZE),Point((x+1)*CELLSIZE,(y+1)*CELLSIZE))

    i = (y-1)*cols + (x-1)
    #print(x, y, i)
    c = cells[i]
    #update adjacent cells
    i_adj = getAdjInd(x,y,line)
    print(i,line,i_adj)
    
    c_adj = cells[i_adj]            
    if c.getLine(line) == False and c_adj.getLine(adjacent[line]) == False:
        c.setLine(line)
        if i_adj != i:
            print("no adjecent")
            c_adj.setLine(adjacent[line])
        l.setOutline(player)
        l.draw(win)
        if player == "blue":
            player = "red"
        else:
            player = "blue"
    else:
        print("position already taken")

    
