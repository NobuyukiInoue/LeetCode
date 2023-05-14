import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        # 266ms - 285ms
        res = 0
        len_row, len_col = len(grid), len(grid[0])
        for i in range(len_row - 2):
            for j in range(len_col - 2):
                n_sum = grid[i][j] + grid[i][j + 1] + grid[i][j + 2] \
                    + grid[i + 1][j + 1] \
                    + grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
                res = max(res, n_sum)
        return res

    def maxSum_3lliner1(self, grid: List[List[int]]) -> int:
        # 266ms - 273ms
        R, C = len(grid), len(grid[0])
        def getHourglassSum(r, c):
            return sum(grid[r][c : c + 3]) + grid[r + 1][c + 1] + sum(grid[r + 2][c : c + 3])
        return max(getHourglassSum(r, c) for r in range(R - 2) for c in range(C - 2))


    def maxSum_3liner2(self, grid: List[List[int]]) -> int:
        # 281ms - 295ms
        R, C = len(grid), len(grid[0])
        getHourglassSum = lambda r, c: sum(grid[r][c : c + 3]) + grid[r + 1][c + 1] + sum(grid[r + 2][c : c + 3])
        return max(getHourglassSum(r, c) for r in range(R - 2) for c in range(C - 2))

def printGrid(title, grid):
    print("{0} = [".format(title))
    for i, _ in enumerate(grid):
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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    
    grid = [[int(col) for col in data.split(",")] for data in flds.split("],[")]
    printGrid("grid", grid)

    sl = Solution()
    time0 = time.time()

    result = sl.maxSum(grid)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
