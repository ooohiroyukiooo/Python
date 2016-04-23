# -*- coding: utf-8 -*-

if __name__ == "__main__":
    
    f = open("read.txt", "r")
    
    for row in f:
        print row
        
    f.close()