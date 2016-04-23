# -*- coding: utf-8 -*-

import hashlib

if __name__ == "__main__":
    
    print hashlib.md5("python-izm").hexdigest()
    print hashlib.sha1("python-izm").hexdigest()