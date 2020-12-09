import sys

fast_inp = lambda: sys.stdin.readline().split('\n')[0]
read_list = lambda: fast_inp().split(' ')
read_listi = lambda: list(map(int, fast_inp().split(' ')))
read_listf = lambda: list(map(float, fast_inp().split(' ')))
read_int = lambda: int(fast_inp())
read_float = lambda: float(fast_inp())
read = lambda: fast_inp()
DEBUG = False





def debug(**kwargs):
    if not DEBUG:
        return
    print('*' * 20)
    for k, v in kwargs.items():
        print(f'\t{k}:{v}\t')
    print('*' * 20)

from collections import defaultdict
graph = defaultdict(list)
visited = defaultdict(bool)
count_needed = defaultdict(defaultdict)
source = "shiny gold"
considered = False
def dfs(bag_name):
    # visited[bag_name] = True
    here = 0
    for neighbor in graph[bag_name]:
        # if not visited[neighbor]:
        print(bag_name + " and " + neighbor)
        print(count_needed[bag_name])
        here += count_needed[bag_name][neighbor]
        here += count_needed[bag_name][neighbor] * dfs(neighbor)
        print(f'now {here}')
    return here

def solve() -> None:
    with open("./day7.txt") as f:
        contents = f.read()


    for line in contents.split('\n'):
        split_contain = line.split('contain')
        outer_bag = split_contain[0]
        outer_bag = ' '.join(outer_bag.split(' ')[:-2])
        other_bags = [' '.join(x.split(' ')[2:-1]).strip() for x in split_contain[1].split(',')]
        counts = []
        for x in split_contain[1].split(','):
            y = x.strip().split(' ')[0]
            if y == 'no':
                counts.append(0)
            else:
                counts.append(int(y))
        for i, inner_bag in enumerate(other_bags):
            if inner_bag == "other":
                continue
            graph[outer_bag].append(inner_bag)
            count_needed[outer_bag][inner_bag] = counts[i]
        # print(graph[outer_bag])
    res = 0
    for bag in list(graph.keys()):
        if not bag.startswith(source):
            continue
        global visited
        visited = defaultdict(bool)
        res += dfs(bag)
    print(res)

t = 1
for _ in range(t):
    solve()