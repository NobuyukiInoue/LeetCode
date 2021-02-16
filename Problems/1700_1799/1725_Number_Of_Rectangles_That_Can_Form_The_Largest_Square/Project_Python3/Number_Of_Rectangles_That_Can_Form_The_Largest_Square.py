# coding: utf-8

import collections
import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        # 168ms
        arr = [min(c) for c in rectangles]
        return arr.count(max(arr))

    def countGoodRectangles2(self, rectangles: List[List[int]]) -> int:
        # 184ms
        dic = collections.Counter(min(rect) for rect in rectangles)
        cnts = list(dic.keys())
        cnts.sort()
        return dic[cnts[-1]]

    def countGoodRectangles3(self, rectangles: List[List[int]]) -> int:
        # 188ms
        return [min(c) for c in rectangles].count(max([min(c) for c in rectangles]))

    def countGoodRectangles4(self, rectangles: List[List[int]]) -> int:
        # 192ms
        max_l = 0
        for c in rectangles:
            max_l = max(max_l,min(c))
        return sum([1 for c in rectangles if max_l == min(c)])

    def countGoodRectangles5(self, rectangles: List[List[int]]) -> int:
        # 5820ms
        return sum([1 for y in rectangles if max([min(x) for x in rectangles]) == min(y)])


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
    flds = temp.replace("[[","").replace("]]","").replace(", ",",").rstrip().split("],[")

    rectangles = [[int(n) for n in fld.split(",")] for fld in flds]
    print("rectangles = {0}".format(rectangles))

    sl = Solution()

    time0 = time.time()

    result = sl.countGoodRectangles(rectangles)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
