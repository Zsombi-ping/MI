import timeit
import numpy as np

        #0  1  2  3  4  5  6  7  8  9
mat = [[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ], # 0
       [ 1, 0, 1, 1, 1, 1, 1, 1, 1, 1 ], # 1
       [ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ], # 2
       [ 1, 1, 1, 1, 0, 1, 1, 1, 1, 1 ], # 3
       [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ], # 4
       [ 1, 1, 1, 1, 1, 0, 1, 1, 1, 1 ], # 5
       [ 1, 0, 1, 1, 1, 1, 1, 1, 0, 1 ], # 6
       [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ], # 7
       [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ], # 8
       [ 0, 1, 1, 1, 1, 0, 1, 1, 1, 1 ], # 9
       [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ], # 10
       [ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ]] # 11

R = 12
C = 10
min_dist = 100000

rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]


def isSafe(mat, visited, x, y):
    global rowNum
    global colNum
    if mat[x][y] == 0:
        return False
    for i in range(len(rowNum)):
        if isValid(x + rowNum[i], y + colNum[i], visited):
            if mat[x + rowNum[i]][y + colNum[i]] == 0:
                return False

    return True


def isValid(x, y, visited):
    global R
    global C
    if x < R and y < C and x >= 0 and y >= 0 and not visited[x][y]:
        return True
    return False


def findShortestPathUtil(mat, visited, x, y, dist):
    global C
    global R
    global rowNum
    global colNum
    global shortest_path

    if y == C-1:
        global min_dist
        min_dist = min(dist, min_dist)
        return

    if dist > min_dist:
        return

    visited[x][y] = True


    for i in range(4):
        if isValid(x + rowNum[i], y + colNum[i], visited) and isSafe(mat, visited, x + rowNum[i], y + colNum[i]):
            findShortestPathUtil(mat, visited, x + rowNum[i], y + colNum[i], dist + 1)

    visited[x][y] = False


def findShPath(mat):
    global min_dist
    global R
    global C

    for i in range(R):
        if mat[i][0] == 1:
            visited = np.full((R, C), 0)

            findShortestPathUtil(mat, visited, i, 0, 0)

            if min_dist == C - 1:
                break

    if min_dist != 100000:
        print("Length of shortest path is: {}".format(min_dist))
    else:
        print("Destination not reachable !")


start = timeit.default_timer()

findShPath(mat)

stop = timeit.default_timer()

print('Time: ', stop - start)
