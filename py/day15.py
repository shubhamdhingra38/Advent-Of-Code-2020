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



def solve_1() -> None:
    contents = ''
    with open('./day15.txt') as f:
        contents = f.read()
    spoken_nums = [int(x) for x in contents.split(',')]
    last_spoken = ddict(lambda x: -1)
    has_spoken_before = ddict(bool)
    for i, num in enumerate(spoken_nums):
        last_spoken[num] = i+1
        if i == len(spoken_nums) - 1:
            has_spoken_before[num] = False
        else:
            has_spoken_before[num] = True
    cnt = len(spoken_nums)
    while cnt != 30000000:
        last = spoken_nums[-1]
        if not has_spoken_before[last]:
            #first time spoken
            has_spoken_before[last] = True
            say = 0
        else:
            #spoken many times
            i1 = cnt
            i2 = last_spoken[last]
            say = i1 - i2
        spoken_nums.append(say)
        last_spoken[last] = cnt
        cnt += 1
    print(spoken_nums[-1])





def solve_2() -> None:
    contents = ''
    with open('./day15.txt') as f:
        contents = f.read()








t = 1
for _ in range(t):
    solve_1()
    #solve_2()

