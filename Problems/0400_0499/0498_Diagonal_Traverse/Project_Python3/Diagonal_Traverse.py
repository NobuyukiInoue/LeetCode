# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        # 196ms
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        res = []
        direction = True
        for i in range(m + n - 1):
            up, down = min(i, m - 1), max(i - n + 1, 0)
            if direction:
                for j in range(up, down - 1, -1):
                    res.append(matrix[j][i - j])
            else:
                for j in range(down, up + 1):
                    res.append(matrix[j][i - j])
            direction = not direction
        return res

    def findDiagonalOrder2(self, matrix: List[List[int]]) -> List[int]:
        # 220ms
        if not matrix:
            return matrix
        i, j = 0,0
        res = []
        up = True
        for _ in range(len(matrix)*len(matrix[0])):
            res.append(matrix[i][j])
            if up:
                if i == 0 and j == len(matrix[0]) - 1:
                    i += 1
                    up = not up
                elif i == 0:
                    j += 1
                    up = not up
                elif j == len(matrix[0]) - 1:
                    i += 1
                    up = not up
                else:
                    i -= 1
                    j += 1
            else:
                if j == 0 and i == len(matrix) - 1:
                    j += 1
                    up = not up
                elif j == 0:
                    i += 1
                    up = not up
                elif i == len(matrix) - 1:
                    j += 1
                    up = not up
                else:
                    i += 1
                    j -= 1
        return res

def printGrid(title, grid):
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

    result = sl.findDiagonalOrder(matrix)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
