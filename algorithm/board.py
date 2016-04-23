# -*- coding: utf-8 -*-
#
# board.py : カラー 盤面の定義
#
#

# 定数
SIZE = 14           # 盤面の大きさ
FIRST_KALAH = 6     # 先手、先手のカラーの位置
SECOND_KALAH = 13   # 後手、後手のカラーの位置
STONE = 72          # 石の個数
EVEN = STONE / 2

MAX_VALUE = 100     # 評価値の最大値
MIN_VALUE = -100    # 評価地の最小値
FIRST_WIN = 99      # 先手勝ち
SECOND_WIN = -99    # 後手勝ち

NORMAL = 0          # 通常の穴に入った場合
KALAH = 1           # KALAH に入った場合
GAMEOVER = 2        # ゲーム終了

# 評価関数の呼び出し回数
count = 0

# 盤面
class Board:
    def __init__(self, b):
        self.board = b[:]

    def __getitem__(self, x):
        return self.board[x]

    def copy(self):
        return Board(self.board)

    # 石を配る
    def distribute(self, turn, pos):
        num = self.board[pos]
        self.board[pos] = 0
        while num > 0:
            pos += 1
            if pos == SIZE: pos = 0
            if (turn == FIRST_KALAH and pos == SECOND_KALAH) or \
               (turn == SECOND_KALAH and pos == FIRST_KALAH): continue
            self.board[pos] += 1
            num -= 1
        return pos

    # 両取りのチェック
    def check_capture(self, turn, pos):
        if (turn == FIRST_KALAH and 0 <= pos <= 5) or \
           (turn == SECOND_KALAH and 7 <= pos <= 12):
            if self.board[pos] == 1 and self.board[12 - pos] > 0:
                # 両取りができる
                num = self.board[12 - pos] + 1
                self.board[turn] += num
                self.board[pos] = 0
                self.board[12 - pos] = 0
                return True
        return False

    # 穴にある石を数える
    def count_stone(self, turn):
        n = 0
        for x in xrange(turn - 6, turn): n += self.board[x]
        return n

    # 石をカラーに入れる
    def put_stone_into_kalah(self, turn):
        n = 0
        for x in xrange(turn - 6, turn):
            n += self.board[x]
            self.board[x] = 0
        self.board[turn] += n
    
    # 終了チェック
    def check_gameover(self):
        if self.count_stone(FIRST_KALAH) == 0:
            self.put_stone_into_kalah(SECOND_KALAH)
            return True
        elif self.count_stone(SECOND_KALAH) == 0:
            self.put_stone_into_kalah(FIRST_KALAH)
            return True
        elif self.board[FIRST_KALAH] > EVEN or \
             self.board[SECOND_KALAH] > EVEN:
            return True
        return False

    # 石を動かす
    def move_stone(self, turn, pos):
        pos = self.distribute(turn, pos)
        self.check_capture(turn, pos)
        if self.check_gameover(): return GAMEOVER
        elif pos == turn: return KALAH
        return NORMAL

    # 評価関数
    def value_func(self):
        global count
        count += 1
        n1 = self.board[FIRST_KALAH]
        n2 = self.board[SECOND_KALAH]
        if n1 > EVEN: return FIRST_WIN
        if n2 > EVEN: return SECOND_WIN
        return n1 - n2

    # 盤面の表示
    def print_board(self):
        print '  ',
        for x in xrange(12, 6, -1):
            print '%2d' % self.board[x],
        print
        print '%2d' % self.board[13],
        print '   ' * 6,
        print '%2d' % self.board[6]
        print '  ',
        for x in xrange(0, 6):
            print '%2d' % self.board[x],
        print

# debug 用
def print_count(): print count