# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        # 44ms
        return min(abs(i - start) for i, v in enumerate(nums) if v == target)

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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    nums = [int(_) for _ in flds[0].split(",")]
    print("nums = {0}".format(nums))
    flds2 = [int(_) for _ in flds[1].split(",")]
    target, start = flds2[0], flds2[1]
    print("target = {0:d}, start = {1:d}".format(target, start))

    sl = Solution()
    time0 = time.time()

    result = sl.getMinDistance(nums, target, start)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
