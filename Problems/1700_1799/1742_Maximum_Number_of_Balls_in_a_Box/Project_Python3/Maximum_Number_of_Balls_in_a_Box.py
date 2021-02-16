# coding: utf-8

import collections
import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        # 388ms
        dic = collections.defaultdict(int)
        maxCount = 0
        for n in range(lowLimit, highLimit + 1):
            digits = 1
            while n > 0:
                digits += n % 10
                n //= 10
            dic[digits] += 1
            if dic[digits] > maxCount:
                maxCount = dic[digits]
        return maxCount

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

    lowLimit, highLimit = int(flds[0]), int(flds[1])
    print("lowLimit = {0:d}, highLimit = {1:d}".format(lowLimit, highLimit))

    sl = Solution()

    time0 = time.time()

    result = sl.countBalls(lowLimit, highLimit)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
