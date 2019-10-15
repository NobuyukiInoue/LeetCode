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
        print("Usage: python %s <testdata.txt>" %(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("%s not found..." %argv[1])
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    str_args = temp.replace(" ","").replace("\",\"","").replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    grid = [[ch for ch in row] for row in flds]
    print("grid = %s" %grid)

    time0 = time.time()

    sl = Solution()
    result = sl.numIslands(grid)
    print("result = %d" %result)

    time1 = time.time()

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
