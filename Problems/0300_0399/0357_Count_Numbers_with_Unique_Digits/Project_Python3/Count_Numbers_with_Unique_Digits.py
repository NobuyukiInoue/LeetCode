# coding: utf-8

import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # 24ms
        if n == 0:
            return 1
        res, h = 10, 9
        for i in range(n - 1):
            res += 9*h
            h *= 8 - i
        return(res)

    def countNumbersWithUniqueDigits2(self, n: int) -> int:
        # 48ms
        if n == 0:
            return 1
        total = 1
        for i in range(1, n + 1):
            prod = 1
            num = 9
            for j in range(i):
                prod *= num
                if j == 0:
                    num += 1
                num -= 1
            total += prod
        return total

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()
    n = int(flds)
    print("n = {0:d}".format(n))

    sl = Solution()

    time0 = time.time()

    result = sl.countNumbersWithUniqueDigits(n)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
