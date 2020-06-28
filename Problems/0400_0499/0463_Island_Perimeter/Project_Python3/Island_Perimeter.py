# coding: utf-8

import os
import sys
import time

class Solution:
#   def islandPerimeter(self, grid: List[List[int]]) -> int:
    def islandPerimeter(self, grid):
        island, redge = 0, 0
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    island += 1
                    if j < col - 1 and grid[i][j + 1] == 1:
                        redge += 1
                    if i < row - 1 and grid[i + 1][j] == 1:
                        redge += 1
        return 4*island - 2*redge

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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()

    flds = str_args.split("],[")
    grid = [[int(col) for col in data.split(",")] for data in flds]
    print("grid = {0}".format(grid))

    sl = Solution()
    time0 = time.time()

    result = sl.islandPerimeter(grid)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
