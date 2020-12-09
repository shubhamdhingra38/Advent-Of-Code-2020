"""
author: Shubham Dhingra
09/12/2020
06:44
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

def has_sum(x, q):
    for i in range(len(q)):
        for j in range(len(q)):
            if i == j: continue
            if q[i] + q[j] == x: return True

    return False

def solve() -> None:
    preamble = 25
    with open('./day9.txt') as f:
        contents = f.read()
    q = deque()
    num = -1
    for idx, line in enumerate(contents.split('\n')):
        i = int(line)
        if idx >= preamble:
            if not has_sum(i, q):
                print(i)
                num = i
                break
            q.popleft()
            q.append(i)
        else:
            q.append(i)


    if num != -1:
        s = 0
        lst = deque()
        for idx, line in enumerate(contents.split('\n')):
            if s == num and len(lst) >= 2:
                print(max(lst) + min(lst))
                break
            i = int(line)
            s += i
            lst.append(i)
            while s > num and len(lst) != 0:
                s -= lst.popleft()



t = read_i()
for _ in range(t):
    solve()

