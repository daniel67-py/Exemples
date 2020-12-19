#!/usr/bin/python3
#-*- coding: utf-8 -*-
import os
import sys
from math import *
from turtle import *

r = Turtle()
r.goto(-400, 0)
r.goto(400, 0)
r.home()
r.goto(0, 400)
r.goto(0, -400)
r.home()

t1 = Turtle()
t2 = Turtle()

t1.color('green')
t2.color('red')

t1.home()
t2.home()

t1.up()
t2.up()

t1.goto(-252, 0)
t2.goto(-252, 0)

for x in range(-252, 252):
    y1 = sin(x / 10) * 100
    y2 = cos(x / 10) * 100
    t1.goto(x, y1)
    t2.goto(x, y2)
    t1.down()
    t2.down()

t1.up()
t2.up()

t1.home()
t2.home()
