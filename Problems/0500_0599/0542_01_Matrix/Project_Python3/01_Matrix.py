# coding: utf-8

import copy
import os
import sys
import time

class Solution:
#   def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
    def updateMatrix(self, matrix):
        # 516ms
        m, n = len(matrix), len(matrix[0])
        dp = matrix[:]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    if i == 0 and j == 0:
                        dp[i][j] = sys.maxsize
                    elif i == 0:
                        dp[i][j] = matrix[i][j - 1] + 1
                    elif j == 0:
                        dp[i][j] = matrix[i - 1][j] + 1
                    else:
                        dp[i][j] = min(matrix[i - 1][j], matrix[i][j - 1]) + 1

        for x in range(m - 1,-1,-1):
            for y in range(n - 1, -1, -1):
                if matrix[x][y] != 0:
                    if x == m - 1 and y == n - 1:
                        matrix[x][y] = dp[x][y]
                    elif x == m - 1:
                        matrix[x][y] = min(dp[x][y], 1 + matrix[x][y + 1])
                    elif y == n - 1:
                        matrix[x][y] = min(dp[x][y], 1 + matrix[x+1][y])
                    else:
                        matrix[x][y] = min(dp[x][y], 1 + min(matrix[x + 1][y], matrix[x][y + 1]))
        return matrix

    def updateMatrix2(self, matrix):
        # 604ms
        m, n = len(matrix), len(matrix[0])
        dp = matrix[:]
        res = copy.deepcopy(matrix)

        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    if i == 0 and j == 0:
                        dp[i][j] = sys.maxsize
                    elif i == 0:
                        dp[i][j] = matrix[i][j - 1] + 1
                    elif j == 0:
                        dp[i][j] = matrix[i - 1][j] + 1
                    else:
                        dp[i][j] = min(matrix[i - 1][j], matrix[i][j - 1]) + 1

        for x in range(m - 1,-1,-1):
            for y in range(n - 1, -1, -1):
                if matrix[x][y] != 0:
                    if x == m - 1 and y == n - 1:
                        res[x][y] = dp[x][y]
                    elif x == m - 1:
                        res[x][y] = min(dp[x][y], 1 + res[x][y + 1])
                    elif y == n - 1:
                        res[x][y] = min(dp[x][y], 1 + res[x+1][y])
                    else:
                        res[x][y] = min(dp[x][y], 1 + min(res[x + 1][y], res[x][y + 1]))
        return res

def printGrid(title, grid):
    if grid is None:
        print("{0} = []".format(title))
        return
    print("{0} = [".format(title))
    for i in range(len(grid)):
        if i == 0:
            print(" [", end = "")
        else:
            print(",[", end = "")
        for j in range(len(grid[i])):
            if j == 0:
                print("{0:d}".format(grid[i][j]), end = "")
            else:
                print(",{0:d}".format(grid[i][j]), end = "")
        print("]")
    print("]")

def printResult(title, result):
    print("{0} = [".format(title))
    for i in range(len(result)):
        print(result[i])
    print("]")

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python {0} <testdata.txt>".format(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("{0} not found...".format(argv[1]))
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = {0}".format(temp))
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip()

    matrix = [[int(col) for col in data.split(",")] for data in flds.split("],[")]
    printGrid("matrix", matrix)
  
    sl = Solution()
    time0 = time.time()

    result = sl.updateMatrix(matrix)

    time1 = time.time()

    printGrid("result", result)
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
