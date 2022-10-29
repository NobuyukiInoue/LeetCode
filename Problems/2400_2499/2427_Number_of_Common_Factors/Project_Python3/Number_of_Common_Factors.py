# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def commonFactors_1liner(self, a: int, b: int) -> int:
        # 35ms 63ms
        return sum(a % i == b % i == 0 for i in range(1, min(a, b) + 1))

    def commonFactors(self, a: int, b: int) -> int:
        # 34ms - 56ms
        ans, limit = 0, min(a, b)
        for i in range(1, limit + 1):
            if a % i == 0 and b % i == 0:
                ans += 1
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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    a, b = int(flds[0]), int(flds[1])

    print("a = {0:d}, b = {1:d}".format(a, b))

    sl = Solution()
    time0 = time.time()

    result = sl.commonFactors(a, b)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
