# -*- coding: utf-8 -*-

import os
import shutil

def showDir(path):
    
    print "==================================="
    for dirpath,dirnames,filenames in os.walk(path):
        for dirname in dirnames:
            print os.path.join(dirpath,dirname)
            
if __name__ == "__main__":
    
    tmpdir = " "
    
    os.mkdir(tmpdir)
    os.makedirs("mkdir1/mkdir2/mkdir3")
    showDir(tmpdir)
    
    os.rmdir("mkdir1/mkdir2/mkdir3")
    showDir(tmpdir)
    
#   os.removedirs(tmpdir)
    shutil.rmtree(tmpdir)