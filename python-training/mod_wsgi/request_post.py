# -*- coding: utf-8 -*-

import cgi

def application(environ, start_response):
    
    start_response("200 OK", [('Content-Type','text/html')])
    
    method = environ.get('REQUEST_METHOD')
    
    print_char = ""
    
    if method == "POST":
        wsgi_input     = environ['wsgi.input']
        content_length = int(environ.get('CONTENT_LENGTH', 0))
        query = cgi.parse_qsl(wsgi_input.read(content_length))
        
        for params in query:
            print_char += params[0] + ":" + params[1] + "<br>"
            
        return print_char
        
    return "pythonでmod_wsgi"