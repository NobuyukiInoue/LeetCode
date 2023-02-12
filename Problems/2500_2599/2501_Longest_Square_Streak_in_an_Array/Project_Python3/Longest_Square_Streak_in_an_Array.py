# coding: utf-8

import collections
import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:

    def longestSquareStreak(self, nums: List[int]) -> int:
        # 913ms - 955ms
        sqr = collections.Counter(sorted(set(nums)))
        for n in sqr:
            while (s := math.isqrt(n))**2 == n and s in sqr:
                sqr[s] += 1
                n = s
        return c if (c := max(sqr.values())) >= 2 else -1

    def longestSquareStreak2(self, nums: List[int]) -> int:
        # Time Limite Exceeded.
        ans = 0
        for num in nums:
            cnt = 1
            l_num = num
            while l_num*l_num in nums:
                l_num = l_num*l_num
                cnt += 1
            ans = max(ans, cnt)
        return -1 if ans == 1 else ans

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
    nums = [int(n) for n in flds.split(",")]
    print("nums = {0}".format(nums))

    sl = Solution()

    time0 = time.time()

    result = sl.longestSquareStreak(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
