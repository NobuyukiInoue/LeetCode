# coding: utf-8

import collections
import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 392ms
        ps = sorted(points, key=lambda e: e[1])
        p0 = ps[0][1]
        res = 1
        for i in range(1, len(ps)):
            if ps[i][0] > p0:
                p0 = ps[i][1]
                res += 1
        return res

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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")

    points = [[int(n) for n in fld.split(",")] for fld in flds]
    print("points = {0}".format(points))

    sl = Solution()

    time0 = time.time()

    result = sl.findMinArrowShots(points)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
