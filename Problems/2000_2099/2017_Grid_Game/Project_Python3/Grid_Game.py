# coding: utf-8

import itertools
import operator
import math
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def gridGame0(self, grid: List[List[int]]) -> int:
        # 1142ms
        top, bottom, res = sum(grid[0]), 0, math.inf
        for g0, g1 in zip(grid[0], grid[1]):
            top -= g0
            res = min(res, max(top, bottom))
            bottom += g1
        return res

    def gridGame(self, grid: List[List[int]]) -> int:
        # https://leetcode.com/problems/grid-game/discuss/1490210/Python-3-one-line-faster-than-greater99
        # 976ms
        return min(map(max, itertools.accumulate(grid[1], initial=0), map(operator.sub, itertools.repeat(sum(grid[0])), itertools.accumulate(grid[0]))))
        """
        arg1 = itertools.repeat(sum(grid[0]))
        arg2 = itertools.accumulate(grid[0])
        temp_r = map(operator.sub, arg1, arg2)
        temp_l = map(max, itertools.accumulate(grid[1], initial=0), temp_r)
        return min(temp_l)
        """

    def gridGame2(self, grid: List[List[int]]) -> int:
        # 1266ms
        n = len(grid[0])
        ans = sys.maxsize
        topSum = sum(grid[0])
        bottomSum = 0
        for i in range(n):
            topSum -= grid[0][i]
            ans = min(ans, max(topSum, bottomSum))
            bottomSum += grid[1][i]
        return ans

    def gridGame3(self, grid: List[List[int]]) -> int:
        # 1385ms
        prefix_r1 = list(itertools.accumulate(grid[0]))
        prefix_r2 = list(itertools.accumulate(grid[1]))
        n = len(grid[0])
        res = sys.maxsize
        for i in range(n):
            top = prefix_r1[-1] - prefix_r1[i]
            bottom = prefix_r2[i - 1] if i > 0 else 0
            secondrobot = max(top, bottom)
            res = min(res, secondrobot)
        return res


    def gridGame_work(self, grid: List[List[int]]) -> int:
        r_max, c_max = len(grid), len(grid[0])

        def helper(i: int, j: int, total: int) -> int:
            total += grid[i][j]
            sum1, sum2 = 0, 0
            if i + 1 < r_max:
                sum1 = helper(i + 1, j, total)
            if j + 1 < c_max:
                sum2 = helper(i, j + 1, total)
            if sum1 > total:
                grid[i + 1][j] = 0
            if sum2 > total:
                grid[i][j + 1] = 0
            return max(total, sum1, sum2)

        _ = helper(0, 0, 0)
        sum2 = helper(0, 0, 0)
        return sum2


def printGrid(title, grid):
    print("{0} = [".format(title))
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

    result = sl.gridGame(grid)

    time1 = time.time()

    print("result = {0:}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
