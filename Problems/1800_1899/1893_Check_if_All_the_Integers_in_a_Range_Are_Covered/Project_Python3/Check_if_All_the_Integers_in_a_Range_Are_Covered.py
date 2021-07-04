# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # 40ms
        return all(any(l <= i <= r for l, r in ranges) for i in range(left, right + 1))

    def isCovered2(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # 40ms
        ints = []
        for i in ranges:
            ints.extend(list(range(max(i[0], left), min(i[1], right) + 1)))
        ints = set(ints)
        for i in range(left, right + 1):
            if not i in ints:
                return False
        return True

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
    flds = temp.replace(" ","").replace("\"","").replace("[[[","").rstrip().split("]],[")

    ranges = [[int(col) for col in data.split(",")] for data in flds[0].split("],[")]
    printGrid("ranges", ranges)
    flds2 = [int(_) for _ in flds[1].replace("]]", "").split(",")]
    left, right = flds2[0], flds2[1]
    print("left = {0:d}, right = {1:d}".format(left, right))

    sl = Solution()
    time0 = time.time()

    result = sl.isCovered(ranges, left, right)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
