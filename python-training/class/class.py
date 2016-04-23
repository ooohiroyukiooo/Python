# -*- coding: utf-8 -*-

class test_class:
    
    def __init__(self,code,name):
        self.code    =    code
        self.name    =    name
        
if __name__ == "__main__":
    
    classList    =    []
    classList.append(test_class(1,"テスト１"))
    classList.append(test_class(2,"テスト２"))
    
    for value in classList:
        print "===== class ====="
        print "code --> " + str(value.code)
        print "code --> " + value.name