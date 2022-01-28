# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 21:09:54 2021

@author: wajee
"""

import random
import importlib
import turtle
from turtle import Turtle , Screen
importlib.reload(turtle)


def random_color():
    
    red=random.randint(0,255)
    green=random.randint(0,255)
    blue=random.randint(0,255)
    colour=(red,green,blue)
    return(colour)


timmy=Turtle()
timmy.shape("turtle")
screen=Screen()
screen.colormode(255)


screen_x,screen_y=screen.screensize()
print(screen_x)

timmy.setheading(180)
timmy.penup()
timmy.forward(screen_y)
timmy.speed("fastest")

timmy.setheading(270)

timmy.forward(250)



for step in range(screen_x):
    
    if(timmy.xcor()>screen_y):
        
        print("You have reached the boundary")
        timmy.penup()
        timmy.setheading(180)
        timmy.forward(2*screen_y)
        timmy.setheading(90)
        timmy.forward(50)
        
    else:
        timmy.pendown()
        timmy.fillcolor(random_color())
        timmy.begin_fill()
        timmy.circle(10)
        timmy.end_fill()
        timmy.penup()
        timmy.setheading(0)
        timmy.forward(50)
    
screen.exitonclick()