#!/usr/bin/python3
#-*- coding: utf-8 -*-
import os
import sys
from turtle import *

class Easy_T:
    def __init__(self,
                 title = "Easy-T Graphic",
                 ret_x = 300,
                 ret_y = 300,
                 graph_x = 500,
                 graph_y = 500,
                 step_x = 10,
                 step_y = 10):
        self.title = title
        self.ret_x = ret_x
        self.ret_y = ret_y
        self.graph_x = graph_x
        self.graph_y = graph_y
        self.step_x = step_x
        self.step_y = step_y
        self.reticule()

    def reticule(self):
        t1 = Turtle()
        t1.hideturtle()
        t1.up()
        t1.goto(-(self.ret_x), 0)
        t1.down()
        t1.goto(self.ret_x, 0)
        t1.up()
        t1.home()
        t1.goto(0, self.ret_y)
        t1.down()
        t1.goto(0, -(self.ret_y))
        t1.up()
        t1.home()

        t1.up()
        t1.goto(-self.ret_x, 0)
        for x in range(-self.ret_x, self.ret_x + self.step_x + 1, self.step_x):
            t1.down()
            t1.dot(3)
            t1.up()
            t1.goto(x, 0)

        t1.goto(0, self.ret_y)
        for y in range(self.ret_y, -self.ret_y - self.step_y - 1, -self.step_y):
            t1.down()
            t1.dot(3)
            t1.up()
            t1.goto(0, y)

        t1.home()
        

        
