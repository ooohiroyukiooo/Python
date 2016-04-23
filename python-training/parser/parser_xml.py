# -*- coding: utf-8 -*-

import xml.dom.minidom

if __name__ == "__main__":
    
    dom = xml.dom.minidom.parse("sample.xml")
    
    print dom.documentElement.tagName  #bookmark
    for node in dom.documentElement.childNodes:
        if node.nodeType == node.ELEMENT_NODE:
            print " " + node.tagName  #site
            
            for node2 in node.childNodes:
                if node2.nodeType == node2.ELEMENT_NODE:
                    print "    " + node2.tagName  #name+google
                    
                    for node3 in node2.childNodes:
                        if node3.nodeType == node3.TEXT_NODE:
                            print "    " + node3.data  #url+http://www.google.co.jp/
                            
    print "-----------------------------------"
    
    for url in dom.getElementsByTagName("url"):
        print url.firstChild.data  #http://google.co.jp/