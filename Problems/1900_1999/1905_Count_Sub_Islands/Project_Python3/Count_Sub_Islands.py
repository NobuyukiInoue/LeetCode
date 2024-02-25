import itertools
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # 2033ms - 2060ms
        res, R, C = 0, len(grid1), len(grid1[0])
        def dfs(x: int, y: int) -> bool:
            isSubIsland = True
            if 0 <= x < R and 0 <= y < C and grid2[x][y] == 1:
                if grid1[x][y] != 1:
                    return False
                grid2[x][y] = -1
                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    isSubIsland &= dfs(x + dx, y + dy)
            return isSubIsland
        for x, y in itertools.product(range(R), range(C)):
            if grid2[x][y] == 1:
                res += dfs(x, y)
        return res

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
    flds = temp.replace(" ","").replace("\"","").replace("[[[","").replace("]]]","").rstrip().split("]],[[")

    grid1 = [[int(col) for col in row.split(",")] for row in flds[0].split("],[")]
    grid2 = [[int(col) for col in row.split(",")] for row in flds[1].split("],[")]
    printGrid("grid1", grid1)
    printGrid("grid2", grid2)

    sl = Solution()
    time0 = time.time()

    result = sl.countSubIslands(grid1, grid2)

    time1 = time.time()

    print("result = {0:d}\n".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
