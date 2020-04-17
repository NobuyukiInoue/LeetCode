# coding: utf-8

import collections
import os
import sys
import time

class Solution:
#   def minPathSum(self, grid: List[List[int]]) -> int:
    def minPathSum(self, grid):
        # 92ms, 104ms
        m, n = len(grid), len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]

    def minPathSum2(self, grid):
        # time limit exceed.
        if grid == None:
            return 0
        m, n = len(grid), len(grid[0])
        res = []
        def helper(i, j, total):
            total += grid[i][j]
            if i == m - 1 and j == n - 1:
                res.append(total)
            if i + 1 < m:
                helper(i + 1, j, total)
            if j + 1 < n:
                helper(i, j + 1, total)

        helper(0, 0, 0)

        return min(res)

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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()

    grid_str = flds.split("],[")
    grid = [[int(col) for col in data.split(",")] for data in grid_str]
    print("grid = {0}".format(grid))

    time0 = time.time()

    sl = Solution()
    result = sl.minPathSum(grid)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
