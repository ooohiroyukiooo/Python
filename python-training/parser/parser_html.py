# -*- coding: utf-8 -*-

import urllib2

if __name__ == "__main__":
    
    url = "http://www.python-izm.com"
    
    htmldata = urllib2.urlopen(url)
    print unicode(htmldata.read(),"utf-8")
    
    htmldata.close()