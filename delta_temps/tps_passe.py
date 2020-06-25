#!/usr/bin/python3
#-*- coding : utf-8 -*-
import os
import sys
from datetime import *
from tkinter import *
from tkinter.messagebox import *

###############################################################################
# ce programme permet de calculer le delta entre le moment présent et une
# date passée ou future.
###############################################################################

###############################################################################
### classe principale
###############################################################################
class Temps(Tk):
    def __init__(self):
        
        # définition de la fenetre principale
        Tk.__init__(self)
        self.title("Temps passé")
        self.resizable(width = False, height = False)
        
        # définition de l'instant présent au démarrage de l'application
        self.instant = datetime.now()
        
        # définition des éléments de l'application
        # les éléments concernant l'instant présent
        self.libelle01 = Label(self, text = "Instant présent :")
        self.libelle01.grid(row = 0, column = 0)
        
        self.date_def = Label(self, text = self.instant)
        self.date_def.grid(row = 0, column = 1)
        
        self.redef_inst = Button(self, text = "Redéfinir instant",
                                 command = self.redef)
        self.redef_inst.grid(row = 1, column = 0, columnspan = 2)
        
        # les éléments concernant l'instant à définir
        self.libelle02 = Label(self, text = "Instant défini :")
        self.libelle02.grid(row = 2, column = 0)
        self.lib_annee = Label(self, text = "Année :")
        self.lib_annee.grid(row = 3, column = 0)
        self.lib_mois = Label(self, text = "Mois :")
        self.lib_mois.grid(row = 4, column = 0)
        self.lib_jour = Label(self, text = "Jour :")
        self.lib_jour.grid(row = 5, column = 0)
        self.lib_heure = Label(self, text = "Heure :")
        self.lib_heure.grid(row = 6, column = 0)
        self.lib_minute = Label(self, text = "Minutes :")
        self.lib_minute.grid(row = 7, column = 0)

        self.ent_annee = Entry(self, width = 10)
        self.ent_annee.grid(row = 3, column = 1)
        self.ent_annee.insert("0", "2000")
        self.ent_mois = Entry(self, width = 10)
        self.ent_mois.grid(row = 4, column = 1)
        self.ent_mois.insert("0", "6")
        self.ent_jour = Entry(self, width = 10)
        self.ent_jour.grid(row = 5, column = 1)
        self.ent_jour.insert("0", "21")
        self.ent_heure = Entry(self, width = 10)
        self.ent_heure.grid(row = 6, column = 1)
        self.ent_heure.insert("0", "21")
        self.ent_minute = Entry(self, width = 10)
        self.ent_minute.grid(row = 7, column = 1)
        self.ent_minute.insert("0", "1")

        self.calcul_delta = Button(self, text = "Calculer le delta",
                                   command = self.delta_calc)
        self.calcul_delta.grid(row = 9, column = 0, columnspan = 2)

        # l'élément qui affichera le résultat calculé
        self.libelle03 = Label(self, text = 'résultat')
        self.libelle03.grid(row = 10, column = 0, columnspan = 2)
        
        # bouclage de la fenetre principale et gestion de l'arret
        self.mainloop()
        try:
            self.destroy()
        except TclError:
            sys.exit()

    ###########################################################################
    ### fonctions relatives à l'application
    ###########################################################################

    # la fonction delta_calc va calculer la différence en récupérant les données
    # renseignées dans l'appli, et les retourner dans l'étiquette du bas de la
    # fenetre principale, en cas de probleme, elle retournera un message d'erreur
    def delta_calc(self):
        try:
            ann = int(self.ent_annee.get())
            mth = int(self.ent_mois.get())
            day = int(self.ent_jour.get())
            hrs = int(self.ent_heure.get())
            mnt = int(self.ent_minute.get())

            jadis = datetime(ann, mth, day, hrs, mnt)
            delta = self.instant - jadis            
            self.libelle03.configure(text = str(delta))
            
        except:
            showwarning("heum...", "il y a un probleme avec la date définie...")

    # la fonction redef va redéfinir l'instant présent, et dans la foulée, va
    # faire appel de la fonction delta_calc pour recalculer la différence
    def redef(self):
        self.instant = datetime.now()
        self.date_def.configure(text = self.instant)
        self.delta_calc()
            
###############################################################################
### execution du programme
###############################################################################
runner = Temps
runner()
