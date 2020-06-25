#!/usr/bin/python3
#-*- coding: utf-8 -*-

def fibonacci():
    n, n1, n2 = 0, 0, 1
    for x in range(0, 30):
        print(n, end = " - ")
        n = n2
        n1, n2 = n2, n1 + n

fibonacci()
