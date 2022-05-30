# coding: utf-8

import collections
import itertools
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # 561ms - 797ms
        cnts = collections.defaultdict(int)
        for a, b in itertools.combinations(nums, 2):
            cnts[a*b] += 1
        ans = 0
        for k, v in cnts.items():
            if v > 1:
                ans += (v*(v - 1)//2)*8
        return ans

    def tupleSameProduct_loop(self, nums: List[int]) -> int:
        # 806ms - 1221ms
        cnts = collections.defaultdict(int)
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                cnts[nums[i]*nums[j]] += 1
        ans = 0
        for k, v in cnts.items():
            if v > 1:
                ans += (v*(v - 1)//2)*8
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
    flds = temp.replace("[","").replace("]","").replace(", ",",").rstrip()
    nums = [int(n) for n in flds.split(",")]
    print("nums = {0}".format(nums))

    sl = Solution()

    time0 = time.time()

    result = sl.tupleSameProduct(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
