## Routage d'URLs
#### ou comment faire pour coller une fonction à un url

Un petit programme utilisant le module wsgiref, et plus particulièrement wsgiref.simple_server. Ce script d'exemple permet de générer des chemins d'accès URL sur le réseau local (LAN) et d'y attribuer un message. C'est très basique volontairement, pour ceux qui veulent comprendre comment faire sans se retrouver avec un tas d'informations d'un coup.  

Pour essayer le script, il suffit de le lancer dans votre IDE... Rien de compliqué. Et une fois que le shell de Python s'affiche, il suffit de lui donner de quoi faire :  
    
    Je commence pas invoquer un objet Mon_Server().
    >>> s = Mon_Server()
  
    Et je lui donne deux urls de routage, ainsi que le contenu à afficher en cas d'appel de l'un ou de l'autre. 
    >>> s.transmission(chemin = "/essai", contenu = "je suis une page d'essai")
    >>> s.transmission(chemin = "/salut", contenu = "Hello World, et Salut à tous !")
  
    Pour finir, je démarre mon objet-serveur.
    >>> s.serve_now()

Et là il suffit d'aller sur votre navigateur et de rentrer dans la barre d'url :  

    localhost:8008/essai
    ou
    localhost:8008/salut

Pour afficher l'une ou l'autre page.  

Pour comprendre le fonctionnement, c'est très simple. Tout d'abord, on créé un objet Mon_Server(). Rien de dingue. La fonction .transmission de l'objet créé permet à chaque appel de remplir une liste (self.deserve) avec un dictionnaire contenant les clés 'chemin' et 'contenu'. Chaque appel rajoute un dictionnaire dans cette liste.  

La fonction .app de la classe permet de gérer le routage en cas de requête à notre serveur qui est à l'écoute par défaut sur le port 8008. Cette fonction va lire le contenu de la liste self.deserve et dès que la variable environ['PATH_INFO'] correspond au contenu de la clé 'chemin' d'un élément de la liste, elle va retourner le contenu de la clé 'contenu' dans le navigateur. Pour approfondir et comprendre le contenu de la variable 'environ', lancez le programme mais invoquez la classe de cette façon par exemple :  

    >>> s = Mon_Server(debuging = True, port = 7777)

Repassez à nouveau les deux .transmission(...) comme dans l'exemple plus haut... Et lancez le serveur avec la commande s.serve_now(). Chaque requête devrait afficher une liste détaillée dans le shell Python de l'ensemble des éléments de la variable 'environ'.  

    >>> s = Mon_Server(debuging = True, port = 7777)
    >>> s.transmission(chemin = "/essai", contenu = "je suis une page d'essai")
    >>> s.transmission(chemin = "/salut", contenu = "Hello World, et Salut à tous")
    >>> s.serve_now()
    serveur actif sur le port : {self.port}...
    Ctrl-C pour arreter le serveur.
    Debug_environment est actif.
    MON_SERVER DEBUG ENVIRONMENT VARIABLES RETURNS
      path info         : /essai
      request method    : GET
      script name       : 
      query string      : 
      content type      : text/plain
      content length    : 
      server name       : daniel-xxxxxxxxxxx
      server port       : 7777
      server protocol   : HTTP/1.1
      wsgi.version      : (1, 0)
      wsgi.input        : <_io.BufferedReader name=7>
      wsgi.url_sheme    : http
      wsgi.errors       : <idlelib.run.PseudoOutputFile object at 0x7f5f22d14e80>
      wsgi.multithread  : True
      wsgi.multiprocess : False
      wsgi.run_once     : False
    127.0.0.1 - - [18/Jul/2020 00:13:29] "GET /essai HTTP/1.1" 200 24

Et voilà, j'espère que l'exemple vous donne une idée de comment exploiter les possibilités en partant de cette base. ;)  

Bonne analyse et à la prochaine !  
Daniel.  


