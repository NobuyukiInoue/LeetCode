import itertools
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        # 76ms
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if j < n - 1 and grid[i][j] == grid[i][j + 1]:
                    return False
                if i < m - 1 and grid[i][j] != grid[i + 1][j]:
                    return False
        return True

    def satisfiesConditions2(self, grid: List[List[int]]) -> bool:
        # 66ms - 71ms
        for a, b in itertools.pairwise(grid[0]):
            if a == b:
                return False
        for s in list(map(set, zip(*grid))):
            if len(s) != 1:
                return False
        return True


def printGrid(title, grid):
    print("{0} = [".format(title))
    for i, _ in enumerate(grid):
        if i == 0:
            print(" [", end = "")
        else:
            print(",[", end = "")
        for j in range(len(grid[i])):
            if j == 0:
                print("{0:2d}".format(grid[i][j]), end = "")
            else:
                print(",{0:2d}".format(grid[i][j]), end = "")
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

    matrix = [[int(col) for col in row.split(",")] for row in flds.split("],[")]
    printGrid("matrix", matrix)

    sl = Solution()
    time0 = time.time()

    result = sl.satisfiesConditions(matrix)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
