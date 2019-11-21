from turtle import *
import math
from random import *
r= Turtle()
colormode(255)
tracer(0)

def createRipple():
    #By rishil Patel
    r.setheading(270) #face south
    for i in range(180): #create a half circle
        r.forward(1)
        r.right(1)
def createWaves():
    #By rishil Patel
    r.pencolor("blue")
    r.fillcolor("blue")
    r.begin_fill()
    r.penup()
    r.goto(475,200) #top right corner
    r.pendown()
    for i in range(4): #create 4 ripples
        createRipple()
    r.setheading(270)
    r.forward(700) #go to bottom left corner
    r.left(90)
    r.forward(1200) #go to bottom right corner
    r.goto(475,200) #go to top right corner
    r.end_fill()

def drawLand():
    #By rishil Patel
    r.penup()
    r.pencolor("light green") #color of the land
    r.begin_fill()
    r.fillcolor("light green")
    r.goto(-500,200) 
    r.pendown()
    r.right(90)
    r.forward(800) 
    r.left(90)
    r.forward(((360/math.pi)*4)+60) #goes to the wave's edge
    r.left(90)
    r.forward(800)
    r.left(90)
    r.forward(((360/math.pi)*4)+60) #goes to the wave's edge
    r.end_fill() #fills half the page with the land
update()
