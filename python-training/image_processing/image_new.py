# -*- coding: utf-8 -*-

import Image

if __name__ == "__main__":
    Image.new("RGB", (100,100)).show()            #黒
    Image.new("RGB", (100,100), (255,0,0)).show() #赤