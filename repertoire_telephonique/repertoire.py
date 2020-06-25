#!/usr/bin/python3
#-*- coding: utf-8 -*-
import os
import sys
import sqlite3
from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *

###############################################################################
### classe principale du répertoire
###############################################################################
class Repertoire(Tk):
    def __init__(self):
        # définition du fichier de base de données
        self.fichier = "carnet.db"
        # définition de la fenetre principale
        Tk.__init__(self)
        self.title("Répertoire")
        self.resizable(width = False, height = False)
        
        # définition des intitulés des différentes rubriques
        etiquette_nom = Label(self, text = "Nom : ")
        etiquette_nom.grid(row = 1, column = 1)
        etiquette_prenom = Label(self, text = "Prénom : ")
        etiquette_prenom.grid(row = 2, column = 1)
        etiquette_telfixe = Label(self, text = "Tél. Fixe : ")
        etiquette_telfixe.grid(row = 3, column = 1)
        etiquette_telport = Label(self, text = "Tél. Port : ")
        etiquette_telport.grid(row = 4, column = 1)
        etiquette_adresse = Label(self, text = "Adresse : ")
        etiquette_adresse.grid(row = 5, column = 1)
        etiquette_postal = Label(self, text = "Code postal : ")
        etiquette_postal.grid(row = 6, column = 1)
        etiquette_ville = Label(self, text = "Ville : ")
        etiquette_ville.grid(row = 7, column = 1)
        etiquette_email = Label(self, text = "Email : ")
        etiquette_email.grid(row = 8, column = 1)
        etiquette_autre = Label(self, text = "Autre : ")
        etiquette_autre.grid(row = 9, column = 1)
        etiquette_note = Label(self, text = "Note : ")
        etiquette_note.grid(row = 10, column = 1)
        etiquette_ident = Label(self, text = "Index : ")
        etiquette_ident.grid(row = 11, column = 1)
        
        # définition des entrées des différentes rubriques
        self.entre_nom = Entry(self, width = 30)
        self.entre_nom.grid(row = 1, column = 2)
        self.entre_prenom = Entry(self, width = 30)
        self.entre_prenom.grid(row = 2, column = 2)
        self.entre_telfixe = Entry(self, width = 30)
        self.entre_telfixe.grid(row = 3, column = 2)
        self.entre_telport = Entry(self, width = 30)
        self.entre_telport.grid(row = 4, column = 2)
        self.entre_adresse = Entry(self, width = 30)
        self.entre_adresse.grid(row = 5, column = 2)
        self.entre_postal = Entry(self, width = 30)
        self.entre_postal.grid(row = 6, column = 2)
        self.entre_ville = Entry(self, width = 30)
        self.entre_ville.grid(row = 7, column = 2)
        self.entre_email = Entry(self, width = 30)
        self.entre_email.grid(row = 8, column = 2)
        self.entre_autre = Entry(self, width = 30)
        self.entre_autre.grid(row = 9, column = 2)
        self.entre_note = Entry(self, width = 30)
        self.entre_note.grid(row = 10, column = 2)
        self.entre_ident = Entry(self, width = 10)
        self.entre_ident.grid(row = 11, column = 2)
        
        # définition des boutons de commandes contenus dans un conteneur Frame
        self.conteneur = Frame(self, relief = SUNKEN, borderwidth = 3)
        self.conteneur.grid(row = 12, column = 1, columnspan = 2, padx = 3, pady = 3)
        self.ajoute = Button(self.conteneur, text = "Ajouter", command = self.ajouter)
        self.ajoute.grid(row = 1, column = 1)
        self.retire = Button(self.conteneur, text = "Retirer", command = self.retirer)
        self.retire.grid(row = 1, column = 2)
        self.modif = Button(self.conteneur, text = "Modifier", command = self.modifier)
        self.modif.grid(row = 1, column = 3)
        self.recherche = Button(self.conteneur, text = "Chercher", command = self.chercher)
        self.recherche.grid(row = 1, column = 4)
        self.montre_tout = Button(self.conteneur, text = "Voir Carnet entier", command = self.voir_tout)
        self.montre_tout.grid(row = 1, column = 5)
        self.zeroing = Button(self.conteneur, text = "R-A-Z", command = self.zero)
        self.zeroing.grid(row = 2, column = 1)
        self.info = Button(self.conteneur, text = "Info", command = self.info)
        self.info.grid(row = 2, column = 2)
        self.quitter = Button(self.conteneur, text = "Quitter", command = self.quit)
        self.quitter.grid(row = 2, column = 3)
        
        # définition d'une zone de texte pour afficher les retours à l'utilisateur
        self.texte = ScrolledText(self, width = 65, height = 20, background = "lightgreen", wrap = "word")
        self.texte.grid(row = 13, column = 1, columnspan = 2)

        # bouclage de la fenetre et gestion de l'erreur de sortie
        self.mainloop()
        try:
            self.destroy()
        except TclError:
            sys.exit()

    ###########################################################################
    ### définition des fonctions de l'application
    ###########################################################################
    def ajouter(self):    # fonction permettant d'ajouter une entrée
        # récupération des valeurs des différentes entrées...
        nouveau = self.recup_valeurs()
        # itération des entrées pour voir si l'une d'elle est vide, et si
        # tel est le cas, remplace le vide par "N/A"
        for x in nouveau.keys():
            if nouveau.get(x) == "":
                nouveau[x] = "n/a"
        # attribution des valeurs du dictionnaire 'nouveau' aux variables suivantes
        nom = nouveau["nom"]
        prenom = nouveau["prenom"]
        telfixe = nouveau["telfixe"]
        telport = nouveau["telport"]
        adresse = nouveau["adresse"]
        postal = nouveau["postal"]
        ville = nouveau["ville"]
        email = nouveau["email"]
        autre = nouveau["autre"]
        note = nouveau["note"]
        # conditions d'acces au fichier
        if os.path.exists(self.fichier) == True: # si la base existe
            # connexion à la base de données
            connexion = sqlite3.connect(self.fichier)
            c = connexion.cursor()
            # compte le nombre d'entrées présente dans la table de la base
            instruction1 = """SELECT COUNT(*) FROM repertoire"""
            c.execute(instruction1)
            nb_entree = c.fetchone()
            # insère une nouvelle entrée dans la table de la base
            instruction2 = f"""INSERT INTO repertoire VALUES ("{nb_entree[0]}", "{nom}", "{prenom}", "{telfixe}", "{telport}", "{adresse}", "{postal}", "{ville}", "{email}", "{autre}", "{note}")"""
            c.execute(instruction2)
            # enregistre et referme la base de données
            connexion.commit()
            connexion.close()
        elif os.path.exists(self.fichier) == False: # si la base n'existe pas
            # création de la base de données
            connexion = sqlite3.connect(self.fichier)
            c = connexion.cursor()
            # création d'une table repertoire comportant les colonnes suivantes...
            instruction1 = """CREATE TABLE repertoire (ident, nom, prenom, telfixe, telport, adresse, postal, ville, email, autre, note)"""
            c.execute(instruction1)
            # compte le nombre d'entrées présente dans la table (pour initialiser à 0)
            instruction2 = """SELECT COUNT(*) FROM repertoire"""
            c.execute(instruction2)
            nb_entree = c.fetchone()
            # insère une nouvelle entrée dans la table de la base
            instruction3 = f"""INSERT INTO repertoire VALUES ("{nb_entree[0]}", "{nom}", "{prenom}", "{telfixe}", "{telport}", "{adresse}", "{postal}", "{ville}", "{email}", "{autre}", "{note}")"""
            c.execute(instruction3)
            # enregistre et referme la base de données
            connexion.commit()
            connexion.close()
        # remise à zéro des entrées et signal que le rajout est ok
        self.zero()
        self.voir(tout)
        showinfo(
            "okay !",
            "Le contact a été rajouté")

    ###########################################################################
    def retirer(self):    # fonction permettant de retirer une entrée
        # récupération de la valeur de l'index à supprimer
        index_a_supprimer = self.entre_ident.get()
        try: # essai de voir si l'index à supprimer est un nombre
            index_a_supprimer = int(index_a_supprimer)
            # conditions d'acces au fichier
            if os.path.exists(self.fichier) == False: # si la base n'existe pas
                showwarning(
                    "Pas possible !",
                    "La base de données spécifiée n'existe pas pour le moment")
            elif os.path.exists(self.fichier) == True: # si la base existe
                connexion = sqlite3.connect(self.fichier)
                c = connexion.cursor()
                try: # essai de supprimer
                    instruction = f"""DELETE FROM repertoire WHERE ident = '{index_a_supprimer}'"""
                    c.execute(instruction)
                    showinfo("Okay", "Le contact a été supprimé !")
                except: # sinon retourne ceci
                    showwarning("heum...", "Impossible de supprimer quoi que ce soit !")
                connexion.commit()
                connexion.close()
        except: # si l'index n'est pas valide
            showwarning("heum...", "Merci de donner un index valide !")
        # vider la zone de texte
        self.zero()
        self.voir_tout()

    ###########################################################################
    def modifier(self):    # fonction permettant de modifier une entrée
        ajout_instruction = ""
        # récupération des valeurs dans un dictionnaire pour pouvoir les itérer par la suite
        recherche = self.recup_valeurs()
        # récupération de la valeur de l'index à modifier
        index = self.entre_ident.get()
        try: # vérifie que l'index est bien un nombre
            index = int(index)
            # recherche de l'entrée qui contient une valeur, et récupération de cette valeur
            # dans la variable ajout_instruction
            for x in recherche.keys():
                if recherche.get(x) != "":
                    ajout_instruction = f"""{x} = "{recherche.get(x)}" """
            # condition d'acces au fichier
            if os.path.exists(self.fichier) == False: # si la base n'existe pas
                showwarning(
                    "Pas possible !",
                    "La base de données spécifié n'existe pas pour le moment")
            elif os.path.exists(self.fichier) == True: # si la base existe
                connexion = sqlite3.connect(self.fichier)
                c = connexion.cursor()
                if ajout_instruction != "" and index != None: 
                    try: # si ajout_instruction et index contiennent une valeur, essai ceci
                        instruction = f"""UPDATE repertoire SET {ajout_instruction} WHERE ident = "{index}" """
                        c.execute(instruction)
                        connexion.commit()
                        connexion.close()
                        showinfo("Okay", f"""Le contact à l'index {index} a été modifié !""")
                    except: # sinon préviens l'utilisateur
                        showwarning("heum...", "Quelquechose ne colle pas -_-")
                else: # si ajout_instruction et / ou index ne contiennent rien, renvoi ceci
                    showwarning("heum...", "Avez vous spécifié quelquechose et / ou un index valide ?")
        except: # si l'index n'est pas valide
            showwarning("heum...", "Merci de donner un index valide !")
        # vider la zone de texte
        self.zero()
        self.voir_tout()

    ###########################################################################
    def chercher(self):    # fonction permettant de chercher une entrée
        ajout_instruction = ""
        # récupération des valeurs dans un dictionnaire pour pouvoir les itérer par la suite
        recherche = self.recup_valeurs()
        # récupération de la valeur à rechercher
        for x in recherche.keys():
            if recherche.get(x) != "":
                ajout_instruction = f"""{x} = "{recherche.get(x)}" """
        # préparation de la zone de texte
        self.texte.delete("1.0", "end-1c")
        # condition d'acces au fichier
        if os.path.exists(self.fichier) == False: # si la base n'existe pas
            showwarning(
                "Pas possible !",
                "La base de données spécifié n'existe pas pour le moment")
        elif os.path.exists(self.fichier) == True: # si la base existe
            # connexion à la base de données
            connexion = sqlite3.connect(self.fichier)
            c = connexion.cursor()
            # si la variable ajout_instruction contient une valeur
            if ajout_instruction != "":
                instruction = f"""SELECT * FROM repertoire WHERE {ajout_instruction} ORDER BY nom"""
                # itération de la table pour sortir chaque entrée contenant cette valeur
                for x in c.execute(instruction):
                    self.texte.insert("end-1c", x)
                    self.texte.insert("end-1c", "\n\n")
                # fermeture de la base de données
                connexion.close()
            else: # si l'utilisateur n'a donné aucune valeur de recherche
                showwarning("heum...", "Donnez moi un minimum à rechercher... -_-")

    ###########################################################################
    def voir_tout(self):    # fonction permettant de voir l'intégralité du carnet trié par noms
        # nettoyage de la zone de texte
        self.texte.delete("1.0", "end-1c")
        # condition d'acces au fichier
        if os.path.exists(self.fichier) == False: # si la base n'existe pas
            showwarning(
                "Pas possible !",
                "La base de données spécifié n'existe pas pour le moment")
        elif os.path.exists(self.fichier) == True: # si la base existe
            # connexion à la base de données
            connexion = sqlite3.connect(self.fichier)
            c = connexion.cursor()
            # itération de la table et affichage trié alphabétiquement par noms
            instruction = """SELECT * FROM repertoire ORDER BY nom"""
            for x in c.execute(instruction):
                self.texte.insert("end-1c", x)
                self.texte.insert("end-1c", "\n\n")
            # fermeture de la base de données
            connexion.close()

    ###########################################################################
    def zero(self):    # fonction permettant de vider les entrées de l'application
        self.entre_nom.delete('0', 'end')
        self.entre_prenom.delete('0', 'end')
        self.entre_telfixe.delete('0', 'end')
        self.entre_telport.delete('0', 'end')
        self.entre_adresse.delete('0', 'end')
        self.entre_postal.delete('0', 'end')
        self.entre_ville.delete('0', 'end')
        self.entre_email.delete('0', 'end')
        self.entre_autre.delete('0', 'end')
        self.entre_note.delete('0', 'end')
        self.texte.delete('1.0', 'end-1c')

    ###########################################################################
    def info(self):    # fonction permettant d'afficher les informations sur l'application
        showinfo(
            "Info...",
            "Répertoire v.0.1 - Developpé par Meyer Daniel pour Linux sous Python 3 - Février 2020")

    ###########################################################################
    def recup_valeurs(self):    # fonction permettant de récupérer les valeurs des entrées
        # récupère les valeurs contenues dans les entrées de l'application
        recuperation = {
            'nom': self.entre_nom.get(),
            'prenom': self.entre_prenom.get(),
            'telfixe': self.entre_telfixe.get(),
            'telport': self.entre_telport.get(),
            'adresse': self.entre_adresse.get(),
            'postal': self.entre_postal.get(),
            'ville': self.entre_ville.get(),
            'email': self.entre_email.get(),
            'autre': self.entre_autre.get(),
            'note': self.entre_note.get()
            }
        # formate certaines valeurs en minuscule
        recuperation['nom'] = recuperation['nom'].lower()
        recuperation['prenom'] = recuperation['prenom'].lower()
        recuperation['adresse'] = recuperation['adresse'].lower()
        recuperation['ville'] = recuperation['ville'].lower()
        recuperation['autre'] = recuperation['autre'].lower()
        recuperation['note'] = recuperation['note'].lower()
        # retourne le tout
        return recuperation

###############################################################################
### lancer l'application
###############################################################################
auto = Repertoire()


    
