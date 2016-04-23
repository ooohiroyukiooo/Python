# -*- coding: utf-8 -*-

import Image

if __name__ == "__main__":
    
    img = Image.open("genome.jpg")
    
    left_right_image = img.transpose(Image.FLIP_LEFT_RIGHT)
    left_right_image.save("genome_left_right.jpg")
    
    top_buttom_image = img.transpose(Image.FLIP_TOP_BOTTOM)
    top_buttom_image.save("genome_top_buttom.jpg")
    
    img.thumbnail((125,25))
    img.save("tumb.jpg")