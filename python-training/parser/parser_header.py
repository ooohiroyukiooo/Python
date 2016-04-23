# -*- coding: utf-8 -*-

import urllib2

if __name__ == "__main__":
    
    url = "http://www.python-izm.com/"
    
    opener = urllib2.build_opener()
    opener.addheaders = [ ('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT5.1; ja; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 ( .NET CLR 3.5.30729)') ]
    
    htmldata = opener.open(url)
    print unicode(htmldata.read(),"utf-8")
    
    htmldata.close()
    opener.close()