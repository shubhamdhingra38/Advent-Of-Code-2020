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

def apply_mask(num, mask) -> int:
    bin_num = bin(num)[2:].rjust(36, '0')
    print(bin_num, 'with', mask)
    res = []
    for i in range(36):
        if mask[i] == '1':
            res.append('1')
        elif mask[i] == 'X':
            res.append(bin_num[i])
        elif mask[i] == '0':
            res.append('0')
    res = ''.join(res)
    return int(res, 2)


def solve_1() -> None:
    contents = ''
    with open('./day14.txt') as f:
        contents = f.read()
    mask = 'X' * 36
    d = ddict(int)
    for line in contents.split('\n')[:-1]:
        if line.startswith('mask'):
            m = line.split(' ')[-1]
            mask = m
            print('mask is now', mask)
        elif line.startswith('mem'):
            s = ''
            i = 4
            while line[i] != ']':
                s += line[i]
                i += 1
            m = line.split(' ')[-1]
            val = int(m)
            new_val = apply_mask(val, mask)
            d[s] = new_val
    s = 0
    for k in d.keys():
        s += d[k]
    print(s)


def generate_all_possible(idx, addr, d, val):
    if idx == len(addr):
        d[''.join(addr)] = val
        print('generated', int(''.join(addr), 2))
        return
    if addr[idx] == 'X':
        addr[idx] = '0'
        generate_all_possible(idx+1, addr, d, val)
        addr[idx] = '1'
        generate_all_possible(idx+1, addr, d, val)
        addr[idx] = 'X'
    else:
        generate_all_possible(idx+1, addr, d, val)

def apply_mask_2(val, mask, d, num) -> list:
    bin_num = bin(val)[2:].rjust(36, '0')
    res = []
    for i in range(36):
        if mask[i] == '1':
            res.append('1')
        elif mask[i] == '0':
            res.append(bin_num[i])
        elif mask[i] == 'X':
            res.append('X')
    print('res', ''.join(res))
    generate_all_possible(0, res, d, num)


def solve_2() -> None:
    contents = ''
    with open('./day14.txt') as f:
        contents = f.read()
    mask = 'X' * 36
    d = ddict(int)
    for line in contents.split('\n')[:-1]:
        if line.startswith('mask'):
            m = line.split(' ')[-1]
            mask = m
            print('mask is now', mask)
        elif line.startswith('mem'):
            s = ''
            i = 4
            while line[i] != ']':
                s += line[i]
                i += 1
            s = int(s)
            m = line.split(' ')[-1]
            val = int(m)
            apply_mask_2(s, mask, d, val)
    s = 0
    for k in d.keys():
        s += d[k]
    print(s)








t = 1
for _ in range(t):
    #solve_1()
    solve_2()

