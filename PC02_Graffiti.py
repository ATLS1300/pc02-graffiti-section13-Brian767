#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
turtle.pensize(10)
turtle.begin_fill()
turtle.fillcolor("red")
turtle.goto(90,90)
turtle.goto(90,-90)
turtle.goto(0,0)
turtle.goto(-90,90)
turtle.goto(-90,-90)
turtle.goto(0,0)
turtle.end_fill()
turtle.penup()
turtle.pencolor("white")
turtle.pensize(2)
turtle.goto(-15,80)
turtle.pendown()
turtle.circle(30)
turtle.penup()
turtle.goto(33,190)
turtle.pendown()
turtle.pencolor("black")
turtle.pensize(15)
turtle.right(180)
turtle.forward(100)
turtle.penup()
turtle.goto(-200,200)
turtle.pendown()
turtle.color(30,100,230)
turtle.pensize(50)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.penup()
turtle.goto(200,0)
turtle.pendown()
turtle.pensize(5)
turtle.pencolor("purple")
turtle.goto(225,50)
turtle.goto(200,100)
turtle.goto(175,50)
turtle.goto(200,0)



#turtle
#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()
