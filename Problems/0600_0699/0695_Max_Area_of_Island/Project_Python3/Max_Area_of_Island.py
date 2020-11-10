# coding: utf-8

import os
import operator
import sys
import time

class Solution:
#   def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    def maxAreaOfIsland(self, grid: [[int]]) -> int:
        # 136ms
        if grid is None or grid[0] is None:
            return 0

        m, n = len(grid), len(grid[0])
        self.ans = 0
        checkTable = grid.copy()

        def dfs(i: int, j: int):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if checkTable[i][j] != 1:
                return
            self.count += 1
            checkTable[i][j] = -1
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
            if self.count > self.ans:
                self.ans = self.count
            return

        for i in range(m):
            for j in range(n):
                self.count = 0
                dfs(i, j)
        return self.ans


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

    grid = [[int(col) for col in data.split(",")] for data in flds.split("],[")]
    printGrid("grid", grid)
  
    sl = Solution()
    time0 = time.time()

    result = sl.maxAreaOfIsland(grid)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
