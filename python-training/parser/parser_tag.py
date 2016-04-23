# -*- coding: utf-8 -*-

import urllib2
from HTMLParser import HTMLParser

class TestParser(HTMLParser):
    
    def __init__(self):
        HTMLParser.__init__(self)
        
    def handle_startag(self,tagname,attribute):
        if tagname.lower() == "a":
            for i in attribute:
                if i[0].lower() == "href":
                    print i[i]
                    
if __name__ == "__main__":
    
    url = "http://www.python-izm.com/"
    
    htmldata = urllib2.urlopen(url)
    
    parser = TestParser()
    #parser.feed(htmldata.read())
    #print htmldata
    data = parser.feed(htmldata.read())
    print data
    
    parser.close()
    htmldata.close()