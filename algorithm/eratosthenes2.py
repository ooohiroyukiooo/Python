# -*- coding: utf-8 -*-

import math

def sieve_of_erastosthenes(num):
    input_list = [False if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 else True for i in range(num)]
    input_list[0] = input_list[1] = False
    input_list[2] = input_list[3] = input_list[5] = True
    sqrt = math.sqrt(num)

    for serial in range(3, num, 2):

        if serial >= sqrt:
            return input_list

        for s in range(serial ** 2, num, serial): 
            input_list[s] = False


if __name__ == '__main__':
    while True:
        try:
            n = int(input())
        except:
            break

        input_list = sieve_of_erastosthenes(n)
        prime_list = [i for i, b in enumerate(input_list) if b == True]
        print(prime_list)
        print(sum(prime_list))