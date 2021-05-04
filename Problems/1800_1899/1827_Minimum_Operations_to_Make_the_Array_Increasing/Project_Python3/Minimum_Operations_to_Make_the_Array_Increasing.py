# coding: utf-8

import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # 112ms
        cnt = prev = 0
        for cur in nums:
            if cur <= prev:
                prev += 1
                cnt += prev - cur
            else:
                prev = cur
        return cnt

    def minOperations2(self, nums: List[int]) -> int:
        # 120ms
        prev = nums[0]
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i] > prev:
                prev = nums[i]
            elif nums[i] == prev:
                prev += 1
                cnt += 1
            else:
                prev += 1
                cnt += prev - nums[i]
        return cnt

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

    result = sl.minOperations(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
