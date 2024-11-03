# Example for VSFX 705 - adapted from 
# From http://home.foni.net/~heikos/data/tkinter.pdf
# added window sizing
# Rosette



import turtle
from turtle import *


def part( total, length, breadth, col ):
    angleInc = 360/total
    width( breadth )
    color( col )
    for i in range(total):
        forward( length )
        left( angleInc )

def rosette( total, length, width, color, angleInc ):
    for i in range( int(360/angleInc) ):
        part( total, length, width, color )
        left( angleInc )

def huan_3(penSize,color,r=50):
    turtle.pensize(penSize)
    turtle.pencolor(color)
    turtle.circle(r)
    

def step(x,y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def notes(contents="",color="black"):
    turtle.pencolor(color)
    turtle.write(arg=contents, move=False, align="left", font=("Arial", 16, "normal"))
    
# set up the turtle
turtle.setup( 500, 500, 100, 100 ) # specify width, height, position on screen
turtle.hideturtle()
turtle.speed(0) # draw as fast as possible

# call the functions
title("画钻石啦")
step(x=0,y=0,)
huan_3(penSize=5,color="#EE9A00",r=47.5)
huan_3(penSize=8,color="#EEAD0E",r=50)
huan_3(penSize=3,color="#EEC900",r=52)
step(x=50,y=70,)
rosette(3,13,0.7,"#8470FF",18)
rosette(5,15,1.3,"#7D26CD",18)
step(x=10,y=-160,)
notes("For my kind-hearted girl .")
step(x=10,y=-180,)
notes("Banrieen 2019-04 .","grey")
turtle.exitonclick()