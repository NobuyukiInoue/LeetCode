# coding: utf-8

import os
import sys
import time

class Solution:
#   def getMaximumGold(self, grid: List[List[int]]) -> int:
    def getMaximumGold(self, grid):
        # 776ms
        mxtotal = 0
        def dfs(total, i, j):
            nonlocal mxtotal
            val = grid[i][j]
            grid[i][j] = 0
            if i + 1 < len(grid) and grid[i + 1][j] != 0:
                dfs(total + val,i + 1,j)
            if i - 1 >= 0 and grid[i - 1][j] != 0:
                dfs(total + val,i - 1, j)
            if j + 1 < len(grid[0]) and grid[i][j + 1] != 0:
                dfs(total + val, i, j + 1)
            if j - 1 >= 0 and grid[i][j - 1] != 0:
                dfs(total + val, i, j - 1)
            mxtotal = max(mxtotal,total + val)
            grid[i][j] = val
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    dfs(0, i, j)
        return mxtotal

    def getMaximumGold2(self, grid):
        # 1012ms
        max = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    count = self.helper(grid, i, j, 0)
                    if count > max:
                        max = count
        return max

    def helper(self, grid, i, j, count):
        if grid[i][j] == 0:
            return count
        count += grid[i][j]
        temp = grid[i][j]
        grid[i][j] = 0

        sum1, sum2, sum3, sum4 = 0, 0, 0, 0
        if i > 0:
            sum1 = self.helper(grid, i - 1, j, count)
        if i < len(grid) - 1:
            sum2 = self.helper(grid, i + 1, j, count)
        if j > 0:
            sum3 = self.helper(grid, i, j - 1, count)
        if j < len(grid[i]) - 1:
            sum4 = self.helper(grid, i, j + 1, count)
        grid[i][j] = temp
        return max(sum1, sum2, sum3, sum4)

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
#   print("grid = {0}".format(grid))
    print("grid = [")
    for i in range(len(grid)):
        if i == 0:
            print(" [", end = "")
        else:
            print(",[", end = "")
        for j in range(len(grid[i])):
            if j == 0:
                print("{0:3d}".format(grid[i][j]), end = "")
            else:
                print(",{0:3d}".format(grid[i][j]), end = "")
        print("]")
    print("]")

    sl = Solution()
    time0 = time.time()
    result = sl.getMaximumGold(grid)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
