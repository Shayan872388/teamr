from turtle import *
R = Turtle()
colormode(255)

def createRipple():
    #By Rishil Patel
    R.setheading(270) #face south
    for i in range(180): #create a half circle
        R.forward(1)
        R.right(1)
def createWaves():
    #By Rishil Patel
    R.pencolor("blue")
    R.fillcolor("blue")
    R.begin_fill()
    R.penup()
    R.goto(475,200) #top right corner
    R.pendown()
    for i in range(4): #create 4 ripples
        createRipple()
    R.setheading(270)
    R.forward(700) #go to bottom left corner
    R.left(90)
    R.forward(1200) #go to bottom right corner
    R.goto(475,200) #go to top right corner
    R.end_fill()

def drawLand():
    #By Rishil Patel
    R.penup()
    R.pencolor("light green") #color of the land
    R.begin_fill()
    R.fillcolor("light green")
    R.goto(-500,200) 
    R.pendown()
    R.right(90)
    R.forward(800) 
    R.left(90)
    R.forward(((360/math.pi)*4)+60) #goes to the wave's edge
    R.left(90)
    R.forward(800)
    R.left(90)
    R.forward(((360/math.pi)*4)+60) #goes to the wave's edge
    R.end_fill() #fills half the page with the land

update()
