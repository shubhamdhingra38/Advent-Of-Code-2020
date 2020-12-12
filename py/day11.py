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

dx = [1, 0, -1]
dy = [1, 0, -1]
def is_valid(i, j, seating):
    if i>=len(seating) or i<0 or j>=len(seating[0]) or j<0:
        return False
    return True

def how_many_occupied(i, j, seating):
    cnt = 0
    for x in [1, 0, -1]:
        for y in [1, 0, -1]:
            f = False
            if x == y and x == 0:
                continue
            pos_x = i
            pos_y = j
            while not f:
                pos_x += x
                pos_y += y
                if not is_valid(pos_x, pos_y, seating):
                    break
                if seating[pos_x][pos_y] == '#' or seating[pos_x][pos_y] == 'L':
                    f = True
                    cnt += 1 if seating[pos_x][pos_y] == '#' else 0

    return cnt

def go_seat(seating):
    changed = False
    org = deepcopy(seating)
    for i in range(len(seating)):
        for j in range(len(seating[0])):
            if org[i][j] == 'L':
                x = how_many_occupied(i, j, org)
                if x == 0:
                    seating[i][j] = '#'
                    changed = True

            elif org[i][j] == '#':
                x = how_many_occupied(i, j, org)
                if x >= 5:
                    seating[i][j] = 'L'
                    changed = True
    return (changed, seating)


def solve() -> None:
    contents = ''
    with open('./day11.txt') as f:
        contents = f.read()

    seating = [list(x) for x in contents.split('\n')]
    seating = seating[:-1]
    print(len(seating), len(seating[0]))
    cnt = 0
    while True:
        changed, seating = go_seat(seating)
        if not changed:
            break
        cnt += 1

    res = 0
    for line in seating:
        res += line.count('#')
    print(res)


t = 1
for _ in range(t):
    solve()

