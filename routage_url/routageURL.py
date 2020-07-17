#!/usr/bin/python
#-*- coding: utf-8 -*-
from wsgiref.simple_server import make_server


class Mon_Server():
    def __init__(self, debuging = False, port = 8008):
        self.debuging = debuging
        self.port = port
        self.environ = ''
        self.deserve = []

    def transmission(self, **from_gss):
        self.deserve.append({
            "chemin": from_gss.get("chemin"),
            "contenu": from_gss.get("contenu"),
            })
        
    def app(self, environ, start_response):
        self.environ = environ
        
        if self.debuging == True:
            self.debug_environment()

        for x in range(0, len(self.deserve)):
            if environ['PATH_INFO'] == self.deserve[x]["chemin"]:
                status = '200 OK'
                headers = [('Content-type', 'text/plain; charset=utf-8')]
                start_response(status, headers)
                ret = [self.deserve[x]["contenu"].encode("utf-8")]
                return ret
    
        status = '200 OK'
        headers = [('Content-type', 'text/plain; charset=utf-8')]
        start_response(status, headers)
        ret = ["heu... c'est quoi cette requête ? o_O grrr...".encode("utf-8")]
        return ret

    def debug_environment(self):
        print('MON_SERVER DEBUG ENVIRONMENT VARIABLES RETURNS')
        print('  path info         : ' + self.environ['PATH_INFO'])
        print('  request method    : ' + self.environ['REQUEST_METHOD'])
        print('  script name       : ' + self.environ['SCRIPT_NAME'])
        print('  query string      : ' + self.environ['QUERY_STRING'])
        print('  content type      : ' + self.environ['CONTENT_TYPE'])
        print('  content length    : ' + self.environ['CONTENT_LENGTH'])
        print('  server name       : ' + self.environ['SERVER_NAME'])
        print('  server port       : ' + self.environ['SERVER_PORT'])
        print('  server protocol   : ' + self.environ['SERVER_PROTOCOL'])
        print('  wsgi.version      : ' + str(self.environ['wsgi.version']))
        print('  wsgi.input        : ' + str(self.environ['wsgi.input']))
        print('  wsgi.url_sheme    : ' + str(self.environ['wsgi.url_scheme']))
        print('  wsgi.errors       : ' + str(self.environ['wsgi.errors']))
        print('  wsgi.multithread  : ' + str(self.environ['wsgi.multithread']))
        print('  wsgi.multiprocess : ' + str(self.environ['wsgi.multiprocess']))
        print('  wsgi.run_once     : ' + str(self.environ['wsgi.run_once']))

    def serve_now(self):
        with make_server('', self.port, self.app) as httpd:
            print(f"serveur actif sur le port : {self.port}...")
            print("Ctrl-C pour arreter le serveur.")
            if self.debuging == True:
                print("Debug_environment est actif.")
            elif self.debuging == False:
                print("Debug_environment est inactif.")
                
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("serveur en cours d'arrêt...")
                httpd.shutdown()
                print("connexion fermée !")

