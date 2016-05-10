#!/usr/bin/python
# -*- coding: utf-8 -*-

import copy
import random
import ReverseCommon
import ReverseBoard
import Game

class Player:
    """ プレーヤの基盤クラス（AIもも含む) """
    
    def __init__(self, color):
        """ コンストラクタ """
        self._color = color
    
    def next_move(self, board):
        """ 次の手を返す """
        pass
    
    @property 
    def color(self):
        """ 自分の色を返す """
        return self._color

class RandomAi(Player):
    """ ランダムで石を置くAI """

    def next_move(self, board):
        all_candidates = ReverseCommon.get_puttable_points(board, self._color)
        # ランダムで次の手を選ぶ
        index = random.randint(0, len(all_candidates) - 1)
        return all_candidates[index]