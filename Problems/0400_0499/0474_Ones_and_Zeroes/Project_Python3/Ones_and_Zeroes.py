# coding: utf-8

import numpy
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 144ms
        dp = numpy.zeros((m + 1, n + 1))
        for s in strs:
            zeros = s.count('0')
            ones = len(s) - zeros
            if zeros > m or ones > n:
                continue
            dp[zeros:m + 1, ones:n + 1] = numpy.maximum(
                dp[zeros:m + 1, ones:n + 1],
                dp[0:m + 1 - zeros, 0:n + 1 - ones] + 1)
        return int(dp[m][n])

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
    flds = temp.replace(" ", "").replace("\"", "").replace("[[", "").replace("]]", "").rstrip().split("],[")

    strs = flds[0].split(",")
    m, n = int(flds[1]), int(flds[2])

    print("strs = {0}, m = {1}, n = {2}".format(strs, m, n))

    sl = Solution()
    time0 = time.time()

    result = sl.findMaxForm(strs, m, n)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
