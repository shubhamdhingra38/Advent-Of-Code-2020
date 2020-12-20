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
import re

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
dx = dy = dz = [1, -1, 0]




def do_for(d_new, d_old, z):
    mat = d_old[z]
    for i in range(len(mat)):
        sub_mat = mat[i]
        for j in range(len(sub_mat)):
            ele = sub_mat[j]
            cnt = 0
            for x_delta in dx:
                for y_delta in dy:
                    for z_delta in dz:
                        if x_delta == y_delta == z_delta == 0: continue
                        #neighbor
                        x = i+x_delta
                        y = j+y_delta
                        z = z+z_delta

                        if z not in d_old:
                            d_new[z] = ddict(ddict)
                            d_old[z] = ddict(ddict)
                        if x not in d_old[z]:
                            d_new[z][x] = ddict(ddict)
                            d_old[z][x] = ddict(ddict)
                        if y not in d_old[z][x]:
                            d_new[z][x][y] = '.'
                            d_old[z][x][y] = '.'
                        if d_old[z][x][y] == '#':
                            cnt += 1
            if ele == '#':
                if cnt == 2 or cnt == 3:
                    continue
                else:
                    d_new[z][i][j] = '.'

            else:
                if cnt == 3:
                    d_new[z][i][j] = '#'

def pprint_dict(d):
    print('+'*10)
    for k in d:
        for x in d[k].values():
            print(x, end = ' ')
        print()
    print('+'*10)



def solve_1() -> None:
    contents = ''
    with open('./day17.txt') as f:
        contents = f.read()
    mat = [list(x) for x in contents.split('\n')[:-1]]
    d = ddict(ddict)
    d[0] = ddict(ddict)
    for i in range(len(mat)):
        if i not in d[0]:
            d[0][i] = ddict(ddict)
        for j in range(len(mat[0])):
            if j not in d[0][i]:
                d[0][i][j] = '.'
            d[0][i][j] = mat[i][j]
    for i in range(6):
        keys = list(d.keys())
        d_before = deepcopy(d)
        for k in keys:
            do_for(d, d_before, k)
        for k in d:
            print('z is', k)
            pprint_dict(d[k])
    c = 0

    for z in d:
        for i in d[z]:
            for j in d[z][i].values():
                if j == '#':
                    c += 1
    print(c)



def solve_2() -> None:
    contents = ''
    with open('./day16.txt') as f:
        contents = f.read()

t = 1
for _ in range(t):
    solve_1()

