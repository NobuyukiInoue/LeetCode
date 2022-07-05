# coding: utf-8

import collections
import os
import operator
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # 192ms
        if not matrix:
            return 0
        hist = [0] * (len(matrix[0]) + 1)
        res = 0
        for row in matrix:
            for i in range(len(row)):
                hist[i] = hist[i] + 1 if int(row[i]) else 0
            res = max(res, self.max_area(hist))
        return res

    def max_area(self, hist):
        stack = collections.deque()
        max_ = 0
        for i, h in enumerate(hist):
            while stack and hist[stack[-1]] > h:
                v = hist[stack.pop()]
                j = stack[-1] + 1 if stack else 0
                max_ = max(max_, v*(i - j))
            stack.append(i)
        return max_

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
    flds = temp.replace(" ", "").replace("\"", "").replace("[[", "").replace("]]", "").rstrip().split("],[")

    if len(flds) == 0 or flds[0] == "[]":
        matrix = []
    else:
        matrix = [[int(col) for col in data.split(",")] for data in flds]
    printGrid("matrix", matrix)

    sl = Solution()
    time0 = time.time()

    result = sl.maximalRectangle(matrix)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
