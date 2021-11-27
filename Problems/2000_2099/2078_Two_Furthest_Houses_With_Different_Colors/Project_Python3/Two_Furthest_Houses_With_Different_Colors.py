# coding: utf-8

import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        # 27ms
        res = 0
        for i, x in enumerate(colors):
            if x != colors[0]:
                res = max(res, i)
            if x != colors[-1]:
                res = max(res, len(colors) - 1 - i)
        return res

    def maxDistance2(self, colors: List[int]) -> int:
        # 28ms
        i, j = 0, len(colors) - 1
        while colors[0] == colors[j]:
            j -= 1
        while colors[-1] == colors[i]:
            i += 1
        return max(len(colors) - 1 - i, j)

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
    flds = temp.replace("[", "").replace("]", "").replace(", ", ",").rstrip()

    colors = [int(n) for n in flds.split(",")]
    print("colors = {0}".format(colors))

    sl = Solution()

    time0 = time.time()

    result = sl.maxDistance(colors)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
