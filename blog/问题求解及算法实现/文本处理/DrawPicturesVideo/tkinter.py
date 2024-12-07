import time      
from tkinter import *
import tkinter as TK

tk=Tk()                                                         #建立一个框架对象tk
canvas=Canvas(tk,width=500,height=500) #建立一个画布对象canvas，属于tk对象
canvas.pack()                                               #将画布对象更新显示在框架中
canvas.create_polygon(10,10,10,60,50,35) 

#建立多边形，顶点坐标（x1,y1,x2,y2,x3,y3），属于canvas对象，

#默认图形编号为1，用于函数调用，以后的图形编号顺序类推。
for i in range(0,60):                 #建立一个60次的循环 ，循环区间[0,59）

    canvas.move(1,5,0)              #canvas对象中的编号“1”图形调用移动函数，x轴5个像素点，y轴不变
    tk.update()                           #更新框架，强制显示改变
    time.sleep(0.05)                   #睡眠0.05秒，制造帧与帧间的间隔时间
for i in range(0,60):                                                   
    canvas.move(1,0,5)
    tk.update()
    time.sleep(0.05)
for i in range(0,60):
    canvas.move(1,-5,0)
    tk.update()
    time.sleep(0.05)
for i in range(0,60):
    canvas.move(1,0,-5)
    tk.update()
    time.sleep(0.05)
