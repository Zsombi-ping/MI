import sys
import numpy as np
import timeit

R = 12
C = 10
min_dist = 100000

rowNum = [-1 , 0  , 0 , 1]
colNum = [0 , -1 , 1 , 0]

def isSafe (mat , visited , x , y):
    if mat [x][y] == 0 or visited[x][y] == True:
        return False
    return True


def isValid (x,y):
    global R
    global C
    if x < R and y < C and x>=0 and y>=0:
        return True
    return False

def markUnsafeCells (mat):
    global R
    global C
    global rowNum
    global colNum

    for i in range (0,R):
        for j in range (0,C):
            if mat[i][j] == 0:
                for k in range (0,4):
                    if isValid(i + rowNum[k], j + colNum[k]):
                        mat[i + rowNum[k]][j + colNum[k]] = -1
                    
    for i in range (0,R):
        for j in range (0,C):
            if mat[i][j] == -1:
                mat[i][j] = 0

def findShortestPathUtil (mat , visited , i , j , dist):
    global C
    global R
    global rowNum
    global colNum

    if j == C-1:
        global min_dist
        min_dist = min(dist , min_dist)
        return
    
    if dist > min_dist:
        return
    
    visited[i][j] = 1

    for k in range (0,4):
        if isValid(i + rowNum[k], j + colNum[k]) and isSafe(mat , visited , i + rowNum[k] , j + colNum[k]):
            findShortestPathUtil(mat , visited , i + rowNum[k], j + colNum[k], dist + 1)
    
    visited[i][j] = 0


def findShPath (mat):

    global min_dist
    global R
    global C

    markUnsafeCells(mat)

    for i in range (0 , R):
        if mat[i][0] == 1:
            visited = np.full((R, C), 0)

            findShortestPathUtil (mat , visited , i , 0 , 0 )

            if min_dist ==  C - 1 :
                break

    if min_dist != 100000:
        print ("Length of shortest path is : ")
        print (min_dist)

    else :
        print ("Destination not reachable !")

    
mat = [ [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 0, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 0, 1, 1, 1, 1 ], 
        [ 1, 0, 1, 1, 1, 1, 1, 1, 0, 1 ], 
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ], 
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ], 
        [ 0, 1, 1, 1, 1, 0, 1, 1, 1, 1 ], 
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ], 
        [ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ]       
      ]



start = timeit.default_timer()

findShPath(mat)

stop = timeit.default_timer()

print('Time: ', stop - start)  