import turtle
from mymath import *


class Graph:
    def __init__(self, minx, miny, maxx, maxy, wx=700, wy=600):
        msx = wx / (maxx - minx)
        msy = wy / (maxy - miny)
        if msx < msy:
            msh = msx
        else:
            msh = msy
        self.mashtab = Vect(msh, msh)
        self.smeschenie = Vect(-0.5 * (maxx - minx) - minx, -0.5 * (maxy - miny) - miny) * msh
        turtle.reset()
        turtle.up()
        self.goto(0, 0)
        turtle.down()

    def color(self, c):
        turtle.color(c)

    def goto(self, x, y=0):
        if type(x) == type(self.mashtab):
            turtle.goto(
                x.x * self.mashtab.x + self.smeschenie.x,
                x.y * self.mashtab.y + self.smeschenie.y)
        else:
            turtle.goto(
                x * self.mashtab.x + self.smeschenie.x,
                y * self.mashtab.y + self.smeschenie.y)

    def drow_curv_blue(self, lines):
        for line in lines:
            self.color(line[6])
            self.goto(line[5])

    def drow_curv_red(self, lines):
        for line in lines:
            x = float(line[2])
            y = float(line[3])
            z = float(line[4])
            if z == 0: self.color("black")
            if z > 0: self.color("green")
            if z < 0: self.color("red")
            self.goto(x, y)
