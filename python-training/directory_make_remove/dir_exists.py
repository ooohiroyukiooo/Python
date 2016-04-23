# -*- coding: utf-8 -*-

import os 

if __name__ == "__main__":

    filepath = "c:/python"
    
    if os.path.exists(filepath):
        print "指定のファイルもしくはディレクトリが存在しています。"
        
        if os.path.isfile(filepath):
            print "指定のパスはファイルです。"
            
        if os.path.isfile(filepath):
            print "指定のパスはディレクトリです。"
    
    else:
        print "指定のファイルもしくはディレクトリが存在していません。"