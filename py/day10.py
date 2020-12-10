"""
author: Shubham Dhingra
10/12/2020
10:26
"""

#===============================================================================================
import sys
import math
from collections import defaultdict as ddict
from collections import deque
import heapq
from queue import Queue
from copy import deepcopy
from bisect import bisect_left as bl
from bisect import bisect_right as br
import os

#==============================================================================================


fast_inp = lambda: sys.stdin.readline().rstrip('\n')
read_l = lambda: fast_inp().split(' ')
read_li = lambda: list(map(int, fast_inp().split(' ')))
read_lf = lambda: list(map(float, fast_inp().split(' ')))
read_i = lambda: int(fast_inp())
read_f = lambda: float(fast_inp())
read = lambda: fast_inp()

#==============================================================================================

DEBUG = True


# DEBUG = False

def debug(**kwargs):
    if not DEBUG:
        return

    print('=' * 20)
    for k, v in kwargs.items():
        print(f'\t{k}:{v}\t')
    print('=' * 20)


#==============================================================================================
"""
Solution starts here
"""

cache = {}
def how_many_ways(num, arr):
    if num not in arr or num > arr[-2]:
        return 0
    elif num == arr[-2]:
        return 1
    if num in cache.keys():
        return cache[num]
    cache[num] = how_many_ways(num+1, arr) + how_many_ways(num+2, arr) + how_many_ways(num+3, arr)
    return cache[num]

def solve() -> None:
    with open('./day10.txt') as f:
        contents = f.read()
    cntOne = 0
    cntThree = 0
    lst = []
    for line in contents.split('\n'):
        i = int(line)
        lst.append(i)
    lst.append(0)
    lst.sort()
    lst.append(lst[-1]+3)
    print(how_many_ways(0, lst))

t = read_i()
for _ in range(t):
    solve()

