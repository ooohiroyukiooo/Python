# -*- coding: utf-8 -*-

def binsearch_rec(target, arr, l, r): 
    """ 再帰で二分探索をする関数
 
    target: 見つけ出したい値
    arr: targetを探索する配列
    l: arrの探索範囲の左端
    r: arrの探索範囲の右端
 
    前提条件: arrは昇順にソートされている必要がある
    戻り値： targetの見つかった位置。見つからなかった場合は-1
    """
 
    if l > r:
        # 探しに探したが見つからなかった
        return -1
 
    m = (l + r) / 2 # 探索範囲の真ん中のindexを計算
    if target < arr[m]:
        # 見つけたい値がarrの真ん中より小さかったら
        # mより左の範囲を再帰的に探す。
        return binsearch_rec(target, arr, l, m-1)
    elif target > arr[m]:
        # 見つけたい値がarrの真ん中より大きかったら
        # mより右の範囲を再帰的に探す。
        return binsearch_rec(target, arr, m+1, r)
    else:
        # 見つけた！
        return m
