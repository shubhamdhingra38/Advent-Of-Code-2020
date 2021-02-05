"""
    The most painful thing and ugliest thing I have ever written.
"""


import math
with open('./input.txt') as f:
    contents = f.read().split('\n\n')

tiles = [] #(ID, tile)
for element in contents:
    ID, *tile = element.split('\n')
    ID = int(ID.split(' ')[1][:-1])
    tiles.append((ID, tile))

n = math.ceil(math.sqrt(len(tiles)))
print("n is ", n)

def printMat(mat):
    for row in mat:
        print(*row)
    print('=' * 20)

def rotateImage90(img):
    rotatedImage = []
    for i in range(len(img[0])):
        row = []
        for j in range(len(img)):
            row.append(img[j][i])
        rotatedImage.append(row[::-1])
    return rotatedImage

def flipImage(img):
    flippedImage = []
    for i in range(len(img))[::-1]:
        row = []
        for j in range(len(img[0])):
            row.append(img[i][j])
        flippedImage.append(row)
    return flippedImage

totalTiles = []
for ID, tile in tiles:
    for i in range(4):
        totalTiles.append((ID, tile))
        tile = rotateImage90(tile)
    tile = flipImage(tile)
    for i in range(4):
        totalTiles.append((ID, tile))
        tile = rotateImage90(tile)


def bordersMatch(mat1, mat2, where):
    if where == 0: #check along last row
        for i in range(len(mat1[0])):
            if mat1[0][i] != mat2[len(mat2)-1][i]:
                return False
    else: #check along last col
        for i in range(len(mat1)):
            if mat1[i][0] != mat2[i][len(mat2[0])-1]:
                return False
    return True

def good(row, col, tile, mat):
    if row != 0 and not bordersMatch(tile, mat[row-1][col], 0):
        return False
    if col != 0 and not bordersMatch(tile, mat[row][col-1], 1):
        return False
    return True

results = set()

foundResult = False
result = -1

def printResult(img):
    for i in range(len(img)):
        matrices = img[i]
        for row in range(len(img[0][0])):
            for mat in matrices:
                for col in range(len(img[0][0])):
                    if col == 0 or col == len(img[0][0]) - 1 or row == 0 or row == len(img[0][0]) - 1:
                        continue
                    print(mat[row][col], end='', sep='')
            print()
        print()
    print("=" * 100)


def matchBorders(row, col, n, usedID, mat):
    global foundResult, result
    if foundResult:
        return
    if row == n and col == 0:
        foundResult = True
        result = usedID[0] * usedID[n-1] * usedID[(n-1)*n] * usedID[(n-1)*n+n-1]
        results.add(result)
        printResult(mat)
        return


    for i, (ID, tile) in enumerate(totalTiles):
        if ID not in usedID:
            if good(row, col, tile, mat):
                usedID.append(ID)
                mat[row][col] = tile

                if col == n - 1:
                    nextRow = row + 1
                    nextCol = 0
                else:
                    nextRow = row
                    nextCol = col + 1

                matchBorders(nextRow, nextCol, n, usedID, mat)
                usedID.pop()


emptyTile = [['.' for _ in range(n)] for __ in range(n)]
mat = [[emptyTile for _ in range(n)] for __ in range(n)]

matchBorders(0, 0, n, [], mat)
print(results)

