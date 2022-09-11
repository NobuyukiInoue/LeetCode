# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        # 139ms - 192ms
        n = len(grid) - 3 + 1
        res = [[0 for _ in range(n)] for _ in range(n)]
        row_max = []
        for row in grid:
            cur = []
            for i in range(n):
                cur.append(max(row[i : i + 3]))
            row_max.append(cur)
        for j, col in enumerate(zip(*row_max)):
            for i in range(n):
                local_max = max(col[i: i + 3])
                res[i][j] = local_max
        return res

    def largestLocal2(self, grid: List[List[int]]) -> List[List[int]]:
        # 235ms - 338ms
        m, n = len(grid), len(grid[0])
        res = []
        for i in range(1, m - 1):
            res.append([])
            for j in range(1, n - 1):
                col_max = -1
                for row in range(i - 1, i + 2):
                    col_max = max(col_max, max(grid[row][j - 1:j + 2]))
                res[-1].append(col_max)
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

    result = sl.largestLocal(grid)

    time1 = time.time()

    print("result = {0}".format(result))
    printGrid("result", result)
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
