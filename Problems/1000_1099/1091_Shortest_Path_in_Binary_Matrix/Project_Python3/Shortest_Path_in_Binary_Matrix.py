import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # 403ms - 409ms
        m, n = len(grid), len(grid[0])
        if grid[0][0] != 0 or grid[m - 1][n - 1] != 0:
            return -1
        visited = [[False for j in range(n)] for i in range(m)]
        que = [(0, 0, 1)]
        while len(que) > 0:
            i, j, dist = que.pop(0)
            if i == m - 1 and j == n - 1:
                return dist
            for di, dj in [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (0, 1), (0, -1), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 0:
                    if visited[ni][nj] is False:
                        visited[ni][nj] = True
                        que.append((ni, nj, dist + 1))
        return -1

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

    result = sl.shortestPathBinaryMatrix(grid)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
