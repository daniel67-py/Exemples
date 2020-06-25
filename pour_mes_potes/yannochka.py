#!/usr/bin/python3
#-*- coding: utf-8 -*-
import os
import sys
from threading import *

###############################################################################
### pour lancer ce script depuis un terminal : python3 yannochka.py
###############################################################################
### avant tout, histoire de camoufler ce script au démarrage...
### nécessite d'avoir xdotool d'installé.
###############################################################################
os.system("xdotool key ctrl+alt+d")

###############################################################################
### programme principal
###############################################################################
class Led_Execute(Thread):
    ### initialisation de la classe permettant le thread
    def __init__(self, instruction):
        Thread.__init__(self)
        self.instruction = instruction
    ### fonction de lancement du thread via méthode .start
    def run(self):
        os.system(self.instruction)

###############################################################################
### volonté de l'utilisateur...
###############################################################################
### ici, défini les applications que tu veux lancer en utilisant le thread que
### j'ai défini plus haut... voilà un exemple :
application_01 = Led_Execute("firefox")
application_02 = Led_Execute("sleep 10")
application_03 = Led_Execute("xed")

### ici tu peux démarrer les threads que tu veux
application_01.start()
application_02.start()

### j'attend que le décompte du thread application_02 soit fini
application_02.join()
### et j'envoi le dernier thread
application_03.start()

###############################################################################
### au final, ce script s'arrêtera automatiquement après le lancement du
### dernier thread !
###############################################################################
