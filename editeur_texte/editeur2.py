#!/usr/bin/python3
#-*- coding: utf-8 -*-
import os
import sys
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.scrolledtext import *

###############################################################################
### edit_py : editeur de texte et programmes en python3 pour Linux
### créé le 12 février 2020 par Meyer Daniel
### modifié le 2à février 2020
### ce programme va finir sur un raspberry dont le système est dépouillé au
### maximum afin d'être le plus léger possible.
###############################################################################

class Edit_Py(Tk):
    def __init__(self):
        self.fichier_en_cours = ""
        # définition de la fenetre principale
        Tk.__init__(self)
        self.title("edit_py ver.0.2")
        self.resizable(width = False, height = False)
        # définition de la zone de texte
        self.texte = ScrolledText(self, background = "lightyellow", undo = True,
                             width = 100, height = 25)
        self.texte.grid(row = 0, column = 0)
        # définition de la barre de menus
        barre_de_menu = Menu(self)
        self['menu'] = barre_de_menu
        # définition des différents menus, surlignage en jaune
        sous_menu_a = Menu(barre_de_menu, tearoff = 0, activebackground = 'yellow')
        sous_menu_b = Menu(barre_de_menu, tearoff = 0, activebackground = 'yellow')
        sous_menu_c = Menu(barre_de_menu, tearoff = 0, activebackground = 'yellow')
        # définition du menu fichier
        barre_de_menu.add_cascade(label = "Fichier", menu = sous_menu_a)
        sous_menu_a.add_command(label = "Nouveau", command = self.nouveau)
        sous_menu_a.add_command(label = "Ouvrir", command = self.ouvrir)
        sous_menu_a.add_separator()
        sous_menu_a.add_command(label = "Sauvegarder", command = self.sauvegarder)
        sous_menu_a.add_command(label = "Sauvegarder sous", command = self.sauvegardersous)
        sous_menu_a.add_separator()
        sous_menu_a.add_command(label = "Quitter", command = self.fin)
        # définition du menu edition
        barre_de_menu.add_cascade(label = "Edition", menu = sous_menu_b)
        sous_menu_b.add_command(label = "Annuler", command = self.annule_modif)
        sous_menu_b.add_command(label = "Revenir", command = self.annule_annul)
        sous_menu_b.add_separator()
        sous_menu_b.add_command(label = "Couper", command = self.coupe)
        sous_menu_b.add_command(label = "Copier", command = self.copie)
        sous_menu_b.add_command(label = "Coller", command = self.colle)
        # définition du menu info
        barre_de_menu.add_cascade(label = "Info", menu = sous_menu_c)
        sous_menu_c.add_command(label = "Info concernant Edit_Py v.0.2", command = self.info)
        # bouclage de la fenetre principale
        self.mainloop()
        try:
            self.destroy()
        except TclError:
            sys.exit()

    ###########################################################################
    ### commandes du menu Fichier
    ###########################################################################
    def nouveau(self):
        # question à l'utilisateur si il souhaite cette action.
        if askokcancel("nouveau fichier ?", "voulez-vous créer un nouveau fichier ?") == True:
            self.fichier_en_cours = ""
            self.texte.delete("1.0", "end-1c")
            self.title("edit_py ver.0.2")
            showwarning("okay !", "page prête, pensez à lui donner un nom ;) ...")        

    def ouvrir(self):
        # boite de dialogue d'ouverture d'un fichier
        fichier = askopenfilename(filetypes = [("texte", ".txt"), ("markdown", ".md"), ("script python", ".py")])
        with open(fichier, "r") as contenu:
            self.texte.delete("1.0", "end-1c")
            self.texte.insert("1.0", contenu.read())
        # modification de la variable globale et affichage du chemin d'acces dans la barre de titre
        self.fichier_en_cours = fichier
        self.title(f"edit_py ver.0.2 - {fichier}")
        self.texte.edit_separator()

    def sauvegarder(self):
        # si fichier_en_cours n'est pas vide
        if self.fichier_en_cours != "":
            with open(fichier_en_cours, "w") as fichier:
                contenu = self.texte.get("1.0", "end-1c")
                contenu.encode("utf-8")
                fichier.write(contenu)
                fichier.close()
            self.texte.edit_separator()
        # sinon renvoi vers la fonction sauvegardersous()
        elif self.fichier_en_cours == "":
            self.sauvegardersous()

    def sauvegardersous(self):
        # boite de dialogue de sauvegarde de fichier
        fichier = asksaveasfilename(filetypes = [("texte", ".txt"), ("markdown", ".md"), ("script python", ".py")])
        with open(fichier, "w") as enregistrement:
            contenu = self.texte.get("1.0", "end-1c")
            contenu.encode("utf-8")
            enregistrement.write(contenu)
            enregistrement.close()
        self.texte.edit_separator()
        self.title(f"edit_py ver.0.2 - {fichier}")
            
    def fin(self):
        # demander l'utilisateur si il souhaite quitter l'application
        if askyesnocancel("fini pour aujourd'hui ?", "voulez vous quitter edit_py ?") == True:
            quit()

    ###########################################################################
    ### commandes du menu Edition
    ###########################################################################
    def coupe(self):
        self.clipboard_clear()                   # vider le presse-papier
        debut = self.texte.index("sel.first")    # ancre de début de sélection
        fin = self.texte.index("sel.last")       # ancre de fin de sélection
        selection = self.texte.get(debut, fin)   # récupération du texte contenu entre les deux ancres
        self.clipboard_append(selection)         # coller le texte dans le presse-papier
        self.texte.delete(debut, fin)            # suppression du texte entre les deux ancres
            
    def copie(self):
        self.clipboard_clear()                   # vider le presse-papier
        debut = self.texte.index("sel.first")    # ancre de début de sélection
        fin = self.texte.index("sel.last")       # ancre de fin de sélection
        selection = self.texte.get(debut, fin)   # récupération du texte contenu entre les deux ancres
        self.clipboard_append(selection)         # coller le texte dans le presse-papier
            
    def colle(self):
        # insert le texte contenu dans le presse-papier à la position ("insert") du curseur
        # d'insertion dans la zone de texte
        self.texte.insert("insert", self.clipboard_get())
                
    def annule_modif(self):
        # annule une action
        self.texte.edit_undo()

    def annule_annul(self):
        # rétablie une action annulée
        self.texte.edit_redo()

    ###########################################################################
    ### commandes du menu Info
    ###########################################################################
    def info(self):
        # montre à l'utilisateur quelques infos relatives à l'application
        showinfo("info : Edit_Py 0.2", "Edit_Py v.0.2, editeur de texte et scripts pour Linux, créé entièrement sous Python 3 par Meyer Daniel - OpenSource - Février 2020")                     

###############################################################################
### execution du programme
###############################################################################
execution = Edit_Py()
execution()

        
    
