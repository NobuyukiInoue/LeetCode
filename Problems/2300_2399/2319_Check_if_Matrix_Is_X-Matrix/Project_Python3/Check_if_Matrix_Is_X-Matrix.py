# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        # 375ms - 519ms
        for i, _ in enumerate(grid):
            for j, _ in enumerate(grid[i]):
                if i == j or i + j == len(grid) - 1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
        return True

    def checkXMatrix_one_loop(self, grid: List[List[int]]) -> bool:
        # 276ms - 596ms
        count_zero = 0
        for i, _ in enumerate(grid[0]):
            if grid[i][i] == 0 or grid[i][len(grid[0])-i-1] == 0:
                return False
            count_zero += grid[i].count(0)
        return count_zero == len(grid[0])*len(grid[0]) - 2*len(grid[0]) + len(grid[0])%2

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

    grid = [[int(col) for col in data.split(",")] for data in flds.split("],[")]
    printGrid("grid", grid)
  
    sl = Solution()
    time0 = time.time()

    result = sl.checkXMatrix(grid)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
