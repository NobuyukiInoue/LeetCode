# coding: utf-8

import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        # 850ms
        return all([len(set(row)) == len(matrix) for row in matrix]) and all([len(set(row)) == len(matrix) for row in zip(*matrix)])

    def checkValid2(self, matrix: List[List[int]]) -> bool:
        # 1002ms
        n = len(matrix)
        for row, col in zip(matrix, zip(*matrix)):
            if len(set(row)) != n or len(set(col)) != n:
                return False
        return True

    def checkValid_bad(self, matrix: List[List[int]]) -> bool:
        for row in matrix:
            check = 0
            for col in row:
                if col == 1:
                    check += 1
                elif col == 2:
                    check += 10
                elif col == 3:
                    check += 100
            if check != 111:
                return False
        for j, _ in enumerate(matrix[0]):
            check = 0
            for i, _ in enumerate(matrix):
                if matrix[i][j] == 1:
                    check += 1
                elif matrix[i][j] == 2:
                    check += 10
                elif matrix[i][j] == 3:
                    check += 100
            if check != 111:
                return False
        return True                

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

    result = sl.checkValid(matrix)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
