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

def evaluate(line: str):
    stack = []
    ops = []
    i = 0
    while i < len(line):
        char = line[i]
        if char.isdigit():
            num_string = ''
            while i + 1 < len(line) and char.isdigit():
                num_string += char
                i += 1
                char = line[i]
            i -= 1
            this = int(num_string)
            if len(stack) != 0 and  stack[-1] != '(' and stack[-1] != ')' and len(ops)!=0:
                other = ops.pop()
                last = stack.pop()
                if last == '*':
                    res = other * this
                elif last == '+':
                    res = other + this
                else:
                    assert False
                ops.append(res)
                print(res)
            else:
                ops.append(int(num_string))
        else:
            if char == '(' or char == '*' or char == '+':
                stack.append(char)
            elif char == ')':
                expr = ''
                while stack[-1] != '(':
                    num = ops.pop()
                    last = stack.pop()
                    expr += str(num) + last
                stack.pop()
                num = ops.pop()
                expr += str(num)
                print("from here got", expr)
                ops.append(evaluate(expr[::-1]))
                this = ops.pop()
                if len(stack) != 0 and  stack[-1] != '(' and stack[-1] != ')' and len(ops)!=0:
                    other = ops.pop()
                    last = stack.pop()
                    if last == '*':
                        res = other * this
                    elif last == '+':
                        res = other + this
                    else:
                        assert False
                    ops.append(res)
                    print(res)
                else:
                    ops.append(this)
        i += 1
    print(ops)
    return ops[-1]







def solve() -> None:
    contents = ''
    with open('./day18.txt') as f:
        contents = f.read()
    answer = 0
    for line in contents.split('\n')[:-1]:
        res = evaluate(line)
        answer += res




t = 1
for _ in range(t):
    solve()

