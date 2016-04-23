# -*- encoding: utf-8 -*-
# gcdは最大降格数（greatest common divisor）の意味

def gcd( x, y ):
    while y != 0:
        x, y = y, x%y
        
print gcd( 24, 12 )
# 実行結果 21