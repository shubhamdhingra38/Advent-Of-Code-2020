from collections import defaultdict
with open('./input.txt') as f:
    lines = f.read().split('\n')

def splitTokens(s):
    directions = []
    i = 0
    while i < len(s):
        if s[i] == 's' or s[i] == 'n':
            directions.append(s[i] + s[i+1])
            i += 2
        else:
            directions.append(s[i])
            i += 1
    return directions

freq = defaultdict(int)
direc_to_tup = defaultdict(tuple)
direc_to_tup['e'] = (0, 1)
direc_to_tup['w'] = (0, -1)
direc_to_tup['nw'] = (1, 0)
direc_to_tup['ne'] = (1, 1)
direc_to_tup['sw'] = (-1, -1)
direc_to_tup['se'] = (-1, 0)

def add(x, y):
    res = [0, 0]
    res[0] = x[0] + y[0]
    res[1] = x[1] + y[1]
    return res


for line in lines:
    mp = defaultdict(int)
    directions = splitTokens(line)
    for direction in directions:
        mp[direction] += 1

    nw = mp['nw']
    ne = mp['ne']
    sw = mp['sw']
    se = mp['se']
    e = mp['e']
    w = mp['w']

    result = (0, 0)
    for k in mp:
        for _ in range(mp[k]):
            result = add(result, direc_to_tup[k])
    # print(result)
    freq[tuple(result)] += 1

nBlack = 0
for key in freq:
    if freq[key] % 2 == 1:
        nBlack += 1
print(nBlack)

def numBlackNeighbors(tile, freqTile):
    nBlack = 0
    for dX, dY in direc_to_tup.values():
        tup = (tile[0] + dX, tile[1] + dY)
        if tup in freqTile and freqTile[tup] % 2 == 1:
            nBlack += 1
    return nBlack


for day in range(100):
    newFreq = defaultdict(int)
    for tile in freq:
        n = numBlackNeighbors(tile, freq)
        whiteNeighbors = [(dX + tile[0], dY + tile[1]) for dX, dY in direc_to_tup.values()]
        if freq[tile] % 2 == 1: #is black
            if n == 0 or n > 2:
                newFreq[tile] = 0
            else:
                newFreq[tile] = 1
        else:
            if n == 2:
                newFreq[tile] = 1
            else:
                newFreq[tile] = 0
        for whiteNeighbor in whiteNeighbors:
            if whiteNeighbor in freq:
                continue
            n = numBlackNeighbors(whiteNeighbor, freq)
            if n == 2:
                newFreq[whiteNeighbor] = 1
            else:
                newFreq[whiteNeighbor] = 0

    freq = newFreq
    cnt = 0
    for key in freq:
        if freq[key] % 2 == 1:
            cnt += 1
    print(f"Day {day} | count {cnt}")




