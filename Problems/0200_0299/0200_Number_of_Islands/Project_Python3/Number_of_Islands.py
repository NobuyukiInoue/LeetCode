# coding: utf-8

import os
import sys
import time

class Solution:
#   def numIslands(self, grid: List[List[str]]) -> int:
    def numIslands(self, grid):
        # 152ms
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    count += 1
                    self.searchIslands(grid, i, j)
        return count
        
    def searchIslands(self, grid, i, j):
        if grid[i][j] == '0':
            return
        grid[i][j] = '0'
        if i - 1 >= 0:
            self.searchIslands(grid, i - 1, j)
        if i + 1 < len(grid):
            self.searchIslands(grid, i + 1, j)
        if j - 1 >= 0:
            self.searchIslands(grid, i, j - 1)
        if j + 1 < len(grid[i]):
            self.searchIslands(grid, i, j + 1)

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
    str_args = temp.replace(" ","").replace("\",\"","").replace("\"","").replace("[[","").replace("]]","").rstrip()

    flds = str_args.split("],[")
    grid = [[ch for ch in row] for row in flds]
    print("grid = {0}",format(grid))

    sl = Solution()
    time0 = time.time()

    result = sl.numIslands(grid)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
