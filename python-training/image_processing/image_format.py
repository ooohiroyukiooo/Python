# -*- coding: utf-8 -*-

import Image

if __name__ == "__main__":
    
    img = open("genome.jpg")
    
    img.save("copy.jpg")
    img.save("logo.bmp","bmp")
    img.save("logo.gif","gif")