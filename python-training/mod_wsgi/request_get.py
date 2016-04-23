# -*- coding: utf-8 -*-

import cgi

def application(environ, start_response):
    
    start_response("200 OK", [('Content-Type','text/html')])
    
    method = environ.get('REQUEST_METHOD')
    
    print_char = ""
    
    if method == "GET":
        query = cgi.parse_qsl(environ.get('QUERY_STRING'))
        
        for params in query:
            print_char += params[0] + ":" + params[1] + "<br>"
            
        return print_char

    return "pythonでmod_wsgi"
