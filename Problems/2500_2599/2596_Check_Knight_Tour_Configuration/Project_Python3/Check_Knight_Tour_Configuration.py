import collections
import itertools
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def checkValidGrid1(self, grid: List[List[int]]) -> bool:
        # 72ms - 75ms
        dic = {}
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                dic[grid[i][j]] = (i, j)
        n = len(grid)**2
        (i, j) = dic[0]
        if i != 0 or j != 0:
            return False
        for idx in range(1, n):
            (n_i, n_j) = dic[idx]
            if abs(n_i - i) == 1 and abs(n_j - j) == 2 \
            or abs(n_i - i) == 2 and abs(n_j - j) == 1:
                (i, j) = (n_i, n_j)
                continue
            return False
        return True

    def checkValidGrid2(self, grid: List[List[int]]) -> bool:
        # 72ms - 75ms
        n, dic = len(grid), collections.defaultdict(tuple)
        if n < 5:
            return n == 1
        notLegal = lambda x, y : {abs(x[0] - y[0]), abs(x[1] - y[1])} != {1, 2}
        for row, col in itertools.product(range(n), range(n)):
            dic[grid[row][col]] = (row,col)
        prev, cnt = (0,0), 1
        while cnt < n*n:
            curr = dic[cnt]
            if notLegal(prev,curr):
                return False
            cnt += 1
            prev = curr
        return True

    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        VALID_MOVES = [
            (-1, -2), (1, -2),
            (-2, -1), (2, -1), (-2, 1), (2, 1),
            (-1, 2), (1, 2)
        ]
        def is_valid(grid: List[List[int]], x: int, y: int, expected_pos: int) -> bool:
            if x >= len(grid) or y >= len(grid[0]) or x < 0 or y < 0 or grid[x][y] != expected_pos:
                return False
            if expected_pos == len(grid) * len(grid[0]) - 1:
                return True
            return any(is_valid(grid, x + dx, y + dy, expected_pos + 1) for dx, dy in VALID_MOVES)
        return is_valid(grid, 0, 0, 0)


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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    
    grid = [[int(col) for col in data.split(",")] for data in flds.split("],[")]
    printGrid("grid", grid)

    sl = Solution()
    time0 = time.time()

    result = sl.checkValidGrid(grid)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
