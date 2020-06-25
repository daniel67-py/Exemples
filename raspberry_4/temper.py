#!/usr/bin/python3
#-*- coding: utf-8 -*-
import os
import sys
from tkinter import *

###############################################################################
### script permettant de suivre la température d'un raspberry pi 4
### script for tracking the temperature of a raspberry pi 4
###############################################################################
class Thermometre(Tk):
    def __init__(self):
        # récupération de la température du raspberry
        # temperature recovery of raspberry
        tmp = open('/sys/class/thermal/thermal_zone0/temp', 'r')
        temperature = tmp.read()
        tmp.close()
        temperature = int(temperature) / 1000
        # définition de la fenetre principale
        # definition of the main window
        Tk.__init__(self)
        self.title("Thermo")
        self.resizable(width = False, height = False)
        self.minsize(width = 200, height = 50)
        # petite mise en forme avec 2 labels
        # putting 2 labels
        self.lib1 = Label(self, text = "Température du Raspberry : ")
        self.lib1.grid(row = 1, column = 1)
        self.lib2 = Label(self, text = temperature)
        self.lib2.grid(row = 1, column = 2)
        # appel de la fonction de mise à jour de la température
        # call of the function who's gonna update the temperature
        self.after(100, self.suivi)
        # un bouton pour quitter proprement...
        # an exit button to finish properly...
        fin = Button(self, text = "Quitter", command = self.destroy)
        fin.grid(row = 2, column = 1, columnspan = 2)
        # et bouclage de l'application
        # and looping the app
        self.mainloop()
        try:
            self.destroy()
        except TclError:
            sys.exit()

    def suivi(self):
        # fonction permettant de remettre à jour la température affichée
        # toutes les 100 millisecondes (0.1sec)
        # function used to update the temperature every 100 milliseconds
        tmp = open('/sys/class/thermal/thermal_zone0/temp', 'r')
        temperature_2 = tmp.read()
        tmp.close()
        temperature_2 = int(temperature_2) / 1000
        self.lib2.configure(text = temperature_2)
        # la fonction se rappelle elle même, cela génère une boucle
        # the function is calling herself back, this will generate a loop
        self.after(100, self.suivi)
        
###############################################################################
### éxécution de l'application / app execution
###############################################################################
run_app = Thermometre()
