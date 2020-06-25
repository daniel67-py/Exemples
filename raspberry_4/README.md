## Thermometre_Rasp4
#### Thermomètre pour Raspberry Pi 4 avec Python 3

Un petit programme permettant de suivre en temps réel la température de son Raspberry Pi 4. Il est basé sur le module tkinter et fait usage de la méthode .after pour permettre la mise à jour de la température après 100 millisecondes. 

Le dossier /sys/class/ des systèmes Raspbian pour Raspberry contient une série de fichiers dans lesquels sont retranscrit les valeurs mesurées de ce genre. Chaque lecture du fichier depuis le script Python donne la valeur à l'instant de la lecture.

-----

#### Thermometer for Raspberry Pi 4 with Python 3

A small program to track the temperature of your Raspberry Pi 4 in real time. It is based on the tkinter module and uses the .after method to update the temperature after 100 milliseconds.

The /sys/class/ folder of Raspbian systems for Raspberry contains a series of files in which are recorded the measured values of this kind. Each reading of the file from the Python script gives the value at the time of reading.

-----

Bonne analyse / Good analysis.

Daniel, le 18 Mars 2020.
