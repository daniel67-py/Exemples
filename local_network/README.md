## partage_dossier / exchange_folder

#### script permettant le partage d'un dossier sur un réseau local en Python3.8

Un petit script permettant de mettre en partage un dossier, tout en laissant le choix du port de sortie à l'utilisateur. Par défaut, le port de sortie sera le 8008, et il sera impossible de choisir un port en-dessous du numéro 1025, ni au dessus du numéro 65535. Il utilise les modules threading, tkinter, socket et http.server et donne un bon exemple concret de l'utilisation d'un thread avec une fenetre tkinter. 

Le script contient deux classes : un thread, permettant d'activer ou de désactiver le serveur Python, et une classe principale contenant la fenetre principale ainsi que les fonctionnalités de celle-ci.

Par sécurité, si l'utilisateur quitte le programme sans refermer le socket de connexion, il sera automatiquement fermé. 

Le but est de pouvoir échanger rapidement des fichiers entre plusieurs pc en réseau. Il suffira pour cela de poser ce script dans le dossier à partager et de le démarrer.

Bonne analyse à tous.

Daniel, le 7 Mars 2020.

------

#### script allowing the share of a folder on a local network in Python3.8

A small script to share a folder, while leaving the choice of output port to the user. By default, the output port will be 8008, and it will be impossible to choose a port below the number 1025, or above the number 65535. It uses the threading, tkinter, socket and http.server modules and gives a good and concrete example of using a thread with a tkinter window.

The script contains two classes: a thread, allowing to activate or deactivate the Python server, and a main class containing the main window as well as its functionalities.

For security, if the user exits the program without closing the connection socket, it will be automatically closed.

The goal is to be able to quickly exchange files between several PCs on the network. You just have to put this script in the folder to share and start it.

Good analysis to all.

Daniel, March 7, 2020.

