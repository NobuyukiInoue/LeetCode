# coding: utf-8

import heapq
import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        # 74ms
        even, odd, res = [], [], []
        for i, num in enumerate(nums):
            if i % 2 == 0:
                heapq.heappush(even, num)
            else:
                heapq.heappush(odd, -num)
        while even and odd:
            res.append(heapq.heappop(even))
            res.append(-heapq.heappop(odd))
        if even:
            res += even
        if odd:
            res += -heapq.heappush(odd)
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
    flds = temp.replace("[","").replace("]","").replace(", ",",").rstrip()

    nums = [int(n) for n in flds.split(",")]
    print("nums = {0}".format(nums))

    sl = Solution()

    time0 = time.time()

    result = sl.sortEvenOdd(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
