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
    with open('./day13.txt') as f:
        contents = f.read()
    s = contents.split('\n')
    i_leave_at = int(s[0])
    bus_schedules = [int(x) if x != 'x' else x for x in s[1].split(',')]
    actual_schedules = []
    for schedule in bus_schedules:
        if schedule == 'x': continue
        actual_schedules.append(schedule)
    print(actual_schedules)
    closest_after = float('inf')
    closest_id = -1
    for s in actual_schedules:
        need_to_wait = 0 if i_leave_at%s == 0 else s - (i_leave_at%s)
        closest_after = min(closest_after, need_to_wait)
        if need_to_wait == closest_after:
            closest_id = s
    print(closest_after * closest_id)


"""
CRT (chinese rem theo)

"""
def crt(mods: list, rems: list) -> int:
    """
    return some x satisfying
    for each i from 1 to n
        x % mods[i] = rems[i]
    """
    n = len(mods)
    pdn = [0] * n #product divided by number for each bucket
    prod = 1
    for i in range(n):
        prod *= mods[i]
    for i in range(n):
        pdn[i] = prod//mods[i]

    print(pdn)
    #all inputs are prime so can use fermats little theorem for mmi
    #each bucket is pdn[i]*rem[i]*mmi(pdn[i], mod[i])
    x = 0
    for i in range(n):
        if i == 0:
            res = 0
        else:
            res = pdn[i] * rems[i] * pow(pdn[i], mods[i]-2, mods[i])
        print(res)
        x += res
    return x % prod


def solve_2() -> None:
    contents = ''
    with open('./day13.txt') as f:
        contents = f.read()
    s = contents.split('\n')
    bus_schedules = [int(x) if x != 'x' else x for x in s[1].split(',')]
    mods = []
    rems = []
    for idx, schedule in enumerate(bus_schedules):
        if schedule == 'x': continue
        mods.append(schedule)
        rems.append(schedule-idx)
    print(crt(mods, rems))








t = 1
for _ in range(t):
    #solve_1()
    solve_2()

