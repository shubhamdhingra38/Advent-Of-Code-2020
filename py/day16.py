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

is_valid = ddict(bool)
good_tickets = []
ticket_rules = ddict(list)
my_ticket = ''
def extract_valid(string):
    res = re.findall(r'\d+-\d+', string)

    name = string.split(':')[0]
    for ranges in res:
        first, second = map(int, ranges.split('-'))
        for i in range(first, second+1):
            is_valid[i] = True
        ticket_rules[name].append((first, second))





def solve_1() -> None:
    global my_ticket
    contents = ''
    with open('./day16.txt') as f:
        contents = f.read()
    splitted = contents.split('\n\n')
    rules = splitted[0].split('\n')
    for rule in rules:
        extract_valid(rule)

    my_ticket = splitted[1]
    other_tickets = splitted[2]
    other_tickets = other_tickets.split('\n')[1:-1]

    _sum = 0
    for ticket in other_tickets:
        ticket_split = list(map(int, ticket.split(',')))
        good = True
        for num in ticket_split:
            if not is_valid[num]:
                _sum += num
                good = False
        if good:
            good_tickets.append(list(ticket_split))


def lies_inside(x, tuple_ranges):
    r1, r2 = tuple_ranges
    return r1[0] <= x <= r1[1] or r2[0] <= x <= r2[1]

def solve_2() -> None:
    global my_ticket
    contents = ''
    with open('./day16.txt') as f:
        contents = f.read()
    my_ticket = list(map(int, my_ticket.split('\n')[1].split(',')))
    good_tickets.append(my_ticket)
    possible = []
    for i in range(len(ticket_rules)):
        possible.append(set())
    for rule_name in ticket_rules:
        for i in range(len(ticket_rules)):
            possible[i].add(rule_name)


    for ticket in good_tickets:
        for idx, num in enumerate(ticket):
            valid_possible_rules = deepcopy(possible[idx])
            for rule in valid_possible_rules:
                ranges = ticket_rules[rule]
                if lies_inside(num, ranges):
                    continue
                else:
                    if rule in possible[idx]:
                        possible[idx].remove(rule)



    considered = ddict(bool)
    while True:
        good = True
        got = ''
        for possibility in possible:
            if len(possibility) == 1:
                #this must be for this rule, remove it from other
                here = list(possibility)[0]
                if considered[here]: continue
                else:
                    considered[here] = True
                    got = here
                    break
        for possibility in possible:
            if len(possibility) != 1:
                good = False
                break
        if good:
            break
        else:
            assert got != ''
            print('got', got)
            for possibility in possible:
                if len(possibility) != 1:
                    if got in possibility:
                        possibility.remove(got)



    for i in range(len(ticket_rules)):
        print('+' * 50)
        print('For rule', i+1)
        for x in possible[i]:
            print(x)

    #beautiful ugly code
    res = 1
    for i in range(len(ticket_rules)):
        assert len(possible[i]) == 1
        what = list(possible[i])[0]
        if what.startswith('departure'):
            res *= my_ticket[i]
    print(res)


t = 1
for _ in range(t):
    solve_1()
    solve_2()

