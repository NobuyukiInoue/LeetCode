# coding: utf-8

import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        # 56ms
        if K%2 == 0 or K%5 == 0:
            return -1
        num, base = 1, 1
        while num%K != 0:
            num = (num*10 + 1)%K
            base += 1
        return base

    def smallestRepunitDivByK2(self, K: int) -> int:
        # 40ms
        if K%2 == 0 or K%5 == 0:
            return -1
        r = 0
        for i in range(1, K + 1):
            r = (r*10 + 1)%K
            if r == 0:
                return i
        return -1

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
    flds = temp.replace("[","").replace("]","").replace(", ",",").rstrip()

    K = int(flds)
    print("K = {0:d}".format(K))

    sl = Solution()

    time0 = time.time()

    result = sl.smallestRepunitDivByK(K)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
