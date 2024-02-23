import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        # 77ms - 87ms
        m, n = len(grid), len(grid[0])
        sorted_rows = [sorted(row) for row in grid]
        return sum([max([sorted_rows[i][j] for i in range(m)]) for j in range(n)])

    def deleteGreatestValue2(self, grid: List[List[int]]) -> int:
        # 79ms - 97ms
        s_grid = []
        for row in grid:
            s_grid.append(row.sort(reverse=True))
        ans = 0
        for j in range(len(grid[0])):
            cur = grid[0][j]
            for i in range(1, len(grid)):
                cur = max(cur, grid[i][j])
            ans += cur
        return ans

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

    grid = [[int(col) for col in row.split(",")] for row in flds.split("],[")]
    printGrid("grid", grid)

    sl = Solution()
    time0 = time.time()

    result = sl.deleteGreatestValue(grid)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
