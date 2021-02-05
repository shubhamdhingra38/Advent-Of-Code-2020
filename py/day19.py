from collections import defaultdict
from os import kill
from typing import DefaultDict, List, Optional
fname = './day19.txt'




"""Some utility functions"""
def is_terminal_rule(rule: str) -> bool:
    if rule.isalpha():
        return True
    return False

def parse_rule(rule: str) -> None:
    rule_num, other = rule.split(':')
    rule_num = int(rule_num)
    global num_to_rules
    other = other.strip()
    if other[0] == "\"":
        other = other.strip("\"")
    num_to_rules[rule_num] = other
    

def util_mul_list(a, b):
    l = []
    for ele in a:
        for ele2 in b:
            l.append(ele+ele2)
    return l


from functools import reduce
def list_cartesian_prod(l: List[List[str]]) -> List[str]:
    return reduce(lambda x, y: util_mul_list(x, y), l)

l = [['a', 'b', 'c'], ['ab', 'bc'], ['xy']]
res = ['aabxy', 'abcxy', 'babxy', 'bbcxy', 'cabxy', 'cbcxy']
assert list_cartesian_prod(l) == res

with open(fname) as f:
    contents = f.read()

rules, strings = contents.split('\n\n')
num_to_rules: List[str] = [''] * 1000
for line in rules.split('\n'):
    parse_rule(line)


num_to_rules_string: List[Optional[List[str]]] = [None] * len(num_to_rules)

#Convert each rule to equivalent string
def get_rule_to_string(num: int):
    if num_to_rules_string[num] != None:
        return num_to_rules_string[num]
    rules = num_to_rules[num]
    if is_terminal_rule(rules):
        num_to_rules_string[num] = [rules]
    else:
        num_to_rules_string[num] = []
        if '|' in rules:
            rules = rules.split('|')
            assert len(rules) == 2
            #Either a or b
            #X -> a | b
            for rule in rules:
                l = []
                for rule_num in rule.split():
                    #here it calls recursively
                    #if rule is a -> b | b a
                    #then it will be infinite loop
                    l.append(get_rule_to_string(int(rule_num)))
                l = list_cartesian_prod(l)
                num_to_rules_string[num].extend(l)
        else:
            possible = []
            for rule in rules.split():
                l = get_rule_to_string(int(rule))
                possible.append(l)
            possible = list_cartesian_prod(possible)
            num_to_rules_string[num].extend(possible)
    return num_to_rules_string[num]



# num_to_rules[8] = '42 | 42 8' (this right recursive so)
# num_to_rules[11] = '42 31 | 42 11 31'



l = get_rule_to_string(0)
l1 = get_rule_to_string(31)
l2 = get_rule_to_string(42)
print(l2)
print()
print(l1)
cnt = 0


k = [len(x) for x in l1][0]
assert(all(len(x) == k for x in l1))
assert(all(len(x) == k for x in l2))


for string in strings.split('\n'):
    org = string
    if string in l:
        cnt += 1
    else:
        if len(string)%k != 0:
            continue
        f1 = f2 = False
        while True:
            matched = False
            for ele in set(l2):
                if string.startswith(ele):
                    matched = True
                    f1 = True
                    string = string[len(ele):]
            if not matched:
                break
        while True:
            matched = False
            for ele in set(l1):
                if string.endswith(ele):
                    string = string[0:len(string)-len(ele)]
                    matched = True
                    f2 = True
            if not matched:
                break
        if f1 and f2:
            if len(string) == 0:
                cnt += 1
            else:
                print('unconsumed', string)

print(cnt)