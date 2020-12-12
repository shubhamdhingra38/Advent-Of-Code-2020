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

def solve() -> None:
    contents = ''
    with open('./day12.txt') as f:
        contents = f.read()
    pos_x = pos_y = 0
    way_point_dir = ('E', 'N')
    way_point_val = [10, 1]
    rotate_waypoint_90R = {('E', 'N'): ('E', 'S'), ('E', 'S'): ('W', 'S'),
            ('W', 'S'): ('W', 'N'), ('W', 'N'): ('E', 'N')}
    sign = {'E': 1, 'N': 1, 'W': -1, 'S': -1}
    rotate_waypoint_90L = {v: k for k, v in rotate_waypoint_90R.items()}


    for instruction in contents.split('\n')[:-1]:
        type = instruction[0]
        val = int(instruction[1:])
        print(instruction)

        if type == 'F':
            pos_x += sign[way_point_dir[0]] * way_point_val[0] * val
            pos_y += sign[way_point_dir[1]] * way_point_val[1] * val
        elif type == 'L':
            times = val // 90
            while times != 0:
                times -= 1
                way_point_dir = rotate_waypoint_90L[way_point_dir]
                way_point_val[0], way_point_val[1] = way_point_val[1], way_point_val[0]
        elif type == 'R':
            times = val // 90
            while times != 0:
                times -= 1
                way_point_dir = rotate_waypoint_90R[way_point_dir]
                way_point_val[0], way_point_val[1] = way_point_val[1], way_point_val[0]
        elif type == 'N':
            way_point_val[1] += val if way_point_dir[1] == 'N' else -val
        elif type == 'E':
            way_point_val[0] += val if way_point_dir[0] == 'E' else -val
        elif type == 'W':
            way_point_val[0] += val if way_point_dir[0] == 'W' else -val
        elif type == 'S':
            way_point_val[1] += val if way_point_dir[1] == 'S' else -val
        if way_point_val[0] < 0:
            way_point_val[0] *= -1
            x_dir, y_dir = way_point_dir
            if x_dir == 'E':
                x_dir = 'W'
            else:
                x_dir = 'E'
            way_point_dir = (x_dir, y_dir)
        elif way_point_val[1] < 0:
            way_point_val[1] *= -1
            x_dir, y_dir = way_point_dir
            if y_dir == 'N':
                y_dir = 'S'
            else:
                y_dir = 'N'
            way_point_dir = (x_dir, y_dir)
        assert way_point_val[0] >= 0 and way_point_val[1] >= 0
        assert way_point_dir[0] in ['E', 'W'] and way_point_dir[1] in ['N', 'S']
        print(pos_x, pos_y)
        print(way_point_dir)
        print(way_point_val)
        print('=' * 50)

    print(pos_x, pos_y)
    print(abs(pos_x) + abs(pos_y))






t = 1
for _ in range(t):
    solve()

