
# -*- coding: UTF-8 -*-
'''
Created on 2018年3月25日

@author: lizhen
'''

import turtle
import time 

def drawPython():
    turtle.setup(650,350,200)
    turtle.penup()
    turtle.fd(-250)
    turtle.pendown()
    turtle.pensize(25)
    turtle.pencolor("purple")
    turtle.seth(-40)
    
    for i in range(40):
        turtle.circle(40,80)
        turtle.circle(-40,80)
        
    turtle.circle(40,80/2)
    turtle.fd(40)
    turtle.circle(16,180)
    turtle.fd(40 * 2/3)
    turtle.down()
    
def turtleWindow():
    turtle.colormode("green")
    turtle.left(45)
    turtle.fd(90)
    turtle.right(135)
    turtle.fd(300)
    turtle.left(135)
    turtle.fd(150)
    turtle.circle(15,5)
    turtle.seth(45)
    #turtle.setup(800,800,0,0)
    #turtle.setup(width=3,height=5, startx=5,starty=5)
    time.sleep(50)
    
if __name__ == "__main__":
    #drawPython()
    turtleWindow()