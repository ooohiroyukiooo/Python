# -*- coding: utf-8 -*-
#
# kalah.py : カラー (アルファベータ法)
#
#
from board import *

# 思考ルーチン

# 先手の指し手
def move_first(depth, board, limit):
    if depth == 0:
        # 盤面の評価
        return board.value_func(), []
    #
    value = MIN_VALUE
    move = []
    for pos in xrange(0, 6):
        if board[pos] == 0: continue
        b = board.copy()
        # 石を動かす
        result = b.move_stone(FIRST_KALAH, pos)
        m = []
        if result == GAMEOVER:
            v = b.value_func()
        elif result == KALAH:
            # 手番は同じまま
            v, m = move_first(depth, b, limit)
        else:
            # 後手番
            v, _ = move_second(depth - 1, b, value)
        # ミニマックス法 : 先手は大きな値を選ぶ
        if value < v:
            value = v
            move = [pos] + m
        # αβ法
        if value >= limit: break
    return value, move

# 後手の指し手
def move_second(depth, board, limit):
    if depth == 0:
        # 盤面の評価
        return board.value_func(), []
    #
    value = MAX_VALUE
    move = []
    for pos in xrange(7, 13):
        if board[pos] == 0: continue
        b = board.copy()
        # 石を動かす
        result = b.move_stone(SECOND_KALAH, pos)
        m = []
        if result == GAMEOVER:
            v = b.value_func()
        elif result == KALAH:
            # 手番は同じまま
            v, m = move_second(depth, b, limit)
        else:
            # 先手番
            v, _ = move_first(depth - 1, b, value)
        # ミニマックス : 後手は小さな値を選ぶ
        if value > v:
            value = v
            move = [pos] + m
        # αβ法
        if value <= limit: break
    return value, move

# 実行
def play(first_depth, second_depth):
    board = Board([6,6,6,6,6,6,0,6,6,6,6,6,6,0])    # 初期状態
    turn = FIRST_KALAH
    while True:
        if turn == FIRST_KALAH:
            value, move = move_first(first_depth, board, MAX_VALUE)
        else:
            value, move = move_second(second_depth, board, MIN_VALUE)
            # 表示
        for x in move:
            print 'move', x
            a = board.move_stone(turn, x)
            board.print_board()
            print
        if a == GAMEOVER:
            print 'Game Over'
            return
        if turn == FIRST_KALAH:
            turn = SECOND_KALAH
        else:
            turn = FIRST_KALAH

# 実行
play(2, 2)
print_count()