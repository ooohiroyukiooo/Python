# -*- coding: utf-8 -*-

import Image

if __name__ == "__main__":

    img = Image.open("genome.jpg")
    
    print img.format
    print img.size
    print img.mode