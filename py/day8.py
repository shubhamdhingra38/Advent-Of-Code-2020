"""
author: Shubham Dhingra
08/12/2020
14:26
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

def has_a_loop(contents):
    n = len(contents)
    visited = ddict(bool)
    i = 0
    acc = 0
    while i < n:
        if visited[i]:
            return True, acc
        visited[i] = True
        instr = contents[i]
        name, does = instr.split(' ')
        if name == 'acc':
            acc += int(does)
            i += 1
        elif name == 'nop':
            i += 1
        elif name == 'jmp':
            i += int(does)
    return False, acc


def solve() -> None:
    with open('./day8.txt') as f:
        contents = f.read().split('\n')


    for i in range(len(contents)):
        instr = contents[i]
        name, does = instr.split(' ')
        if name == 'nop':
            contents[i] = 'jmp' + ' ' + does
        elif name == 'jmp':
            contents[i] = 'nop' + ' ' + does
        f, acc = has_a_loop(contents)
        if not f:
            print(acc)
            break
        else:
            contents[i] = instr


t = read_i()
for _ in range(t):
    solve()

