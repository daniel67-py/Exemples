## repertoire_telephonique / phone_book

#### un répertoire téléphonique en Python3.8 utilisant tkinter et SQLite3.

Après une bonne semaine d'absence, me voici de retour avec un petit programme qui permet de gérer un répertoire téléphonique. Les modules utilisés sont tkinter et sqlite3, et la mise en oeuvre se fait via une classe qui contient le programme. Les fonctions sont basiques : ajouter une entrée, retirer une entrée, modifier une entrée, recherche une valeur dans les entrées de la base de données, voir le contenu de la table de la base de données, et remettre à zéro les champs de l'application.

Il faut savoir certaines choses avant de l'utiliser cette version de base:
- Il n'est possible de modifier qu'une valeur d'une entrée à la fois, et il est impératif de préciser l'index de l'entrée à modifier.
- Lors d'un ajout, toutes les lettres sont mises en minuscules, afin de formater le contenu de la base et ainsi faciliter les recherches par la suite (pour ne pas tenir compte de la case), mis à part le champ contenant l'adresse email, les numéros de téléphones et le code postal.
- Lors d'un ajout, le contenu du champ 'index' n'est pas pris en compte, car le contenu de cette valeur se fera par comptage du nombre d'entrées déjà présentes dans la table (indexage par ordre d'insertion : autoincrémentation).
- La fonction permettant de voir l'intégralité du répertoire fait un tri alphabétique des noms, et non des numéros d'indexation.

Voilà dans les grandes lignes ce qu'il y a à savoir. Une bonne analyse du programme à tous, et à une prochaine !

Daniel, 1 Mars 2020

------

#### a phone book in Python3.8 using tkinter and SQLite3.

After a good week of absence, here I am back with a small program that allows you to manage a telephone directory. The modules used are tkinter and sqlite3, and the implementation is done via a class which contains the program. The functions are basic: add an entry, remove an entry, modify an entry, search for a value in the database entries, see the content of the database table, and reset the fields in the application.

There are a few things you should know before using this basic version:
- It is only possible to modify one value of an entry at a time, and it is imperative to specify the index of the entry to be modified.
- When adding, all letters are put in lowercase, in order to format the content of the database and thus facilitate subsequent searches (to ignore the box), except for the field containing the email address, telephone numbers and postal code.
- When adding, the content of the 'index' field is not taken into account, because the content of this value will be done by counting the number of entries already present in the table (indexing by order of insertion : autoincrement) .
- The function allowing to see the whole directory makes an alphabetical sorting of the names, and not of the indexing numbers.

This is in broad outline what there is to know. A good analysis of the program to all, and see you soon!

Daniel, March 1, 2020

