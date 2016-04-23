# -*- coding: utf-8 -*-

import sys
import math

if __name__ == '__main__':
    # 標準入力
    # 1行に数値を1つ入力
    # 入力終了は Ctrl + Z を押して Enter (for Windows)
    input_list = sys.stdin.readlines()

    for num in input_list:
        num = int(num.replace('\n', ''))

        if 2 > num:
            continue

        # 1. 入力値の連番リストを作成
        # 2, 3, 5の倍数はあらかじめ除去
        multiple_list = [2, 3, 5]
        serial_number_list = [r for r in range(2, num + 1) if r % 2 != 0 and r % 3 != 0 and r % 5]

        # 5. 連番リストの先頭が、入力値の平方根以上で終了
        while math.sqrt(num) >= serial_number_list[0]:

            # 2. 連番を倍数リストに格納
            multiple_list.append(serial_number_list[0])

            # 4. 連番リストの末端まで繰り返す
            for serial_number in range(serial_number_list[0], serial_number_list[- 1] + 1,  serial_number_list[0]):

                if serial_number in serial_number_list:

                    # 3. 連番リストから連番の倍数を除去
                    serial_number_list.remove(serial_number)

        # 6. 連番リストと倍数リストに残った数値が素数
        print(multiple_list + serial_number_list)