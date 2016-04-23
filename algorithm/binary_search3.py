# -*- coding: utf-8 -*-

import bisect


def bisection(t, target):
    """
    takes a sorted list (t) and the (target) value.
    returns the index of the (target) value in the list (t) if there
    is ,otherwise returns None
    """
    i = bisect.bisect_left(t, target)
    if i < len(t) and t[i] == target:
        return i
    else:
        return None


def binary_search(t, target, lo=0, hi=None):
    """binary search 
    takes a sorted list (t) and the (target) value and
    returns the index of the (target) value in the list (t) if there
    is ,otherwise returns None
    (lo):low
    (hi):high
    """
    if not hi: hi = len(t)
    if not lo < hi: return None
    i = (lo + hi) / 2
    if t[i] == target:
        return i
    if t[i] > target:
        # left search
        return binary_search(t, target, lo, i - 1)
    else:
        # right search
        return binary_search(t, target, i + 1, hi)