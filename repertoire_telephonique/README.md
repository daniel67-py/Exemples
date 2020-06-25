## repertoire_telephonique

#### un répertoire téléphonique en Python3.8 utilisant tkinter et SQLite3.

Après une bonne semaine d'absence, me voici de retour avec un petit programme qui permet de gérer un répertoire téléphonique. Les modules utilisés sont tkinter et sqlite3, et la mise en oeuvre se fait via une classe qui contient le programme. Les fonctions sont basiques : ajouter une entrée, retirer une entrée, modifier une entrée, recherche une valeur dans les entrées de la base de données, voir le contenu de la table de la base de données, et remettre à zéro les champs de l'application.

Il faut savoir certaines choses avant de l'utiliser cette version de base:
- Il n'est possible de modifier qu'une valeur d'une entrée à la fois, et il est impératif de préciser l'index de l'entrée à modifier.
- Lors d'un ajout, toutes les lettres sont mises en minuscules, afin de formater le contenu de la base et ainsi faciliter les recherches par la suite (pour ne pas tenir compte de la case), mis à part le champ contenant l'adresse email, les numéros de téléphones et le code postal.
- Lors d'un ajout, le contenu du champ 'index' n'est pas pris en compte, car le contenu de cette valeur se fera par comptage du nombre d'entrées déjà présentes dans la table (indexage par ordre d'insertion).
- La fonction permettant de voir l'intégralité du répertoire fait un tri alphabétique des noms, et non des numéros d'indexation.

Voilà dans les grandes lignes ce qu'il y a à savoir. Une bonne analyse du programme à tous, et à une prochaine !

Daniel, 1 Mars 2020
