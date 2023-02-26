# coding: utf-8

import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        # 1671ms - 1695ms
        cnts = collections.defaultdict(int)
        ans = 0
        for rect in rectangles:
            ans += cnts[rect[0] / rect[1]]
            cnts[rect[0] / rect[1]] += 1
        return ans

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

    rectangles = [[int(col) for col in data.split(",")] for data in flds.split("],[")]
    print("rectangles = {0}".format(rectangles))

    sl = Solution()
    time0 = time.time()

    result = sl.interchangeableRectangles(rectangles)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
