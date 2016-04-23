# -*- coding: utf-8 -*-

import threading
import time
import datetime

class TestThread(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
        print "  === start sub thread ==="
        for i in range(5):
            time.sleep(5)
            print " sub thread : " + str(datetime.datetime.today())
        print "  === end sub thread ==="
        
if __name__ == "__main__":
    
    th = TestThread()
    th.start()
    
    time.sleep(1)
    
    print "=== start main thread ==="
    for i in range(5):
        time.sleep(10)
        print "main thread : " + str(datetime.datetime.today())
    print "=== end main thread ==="