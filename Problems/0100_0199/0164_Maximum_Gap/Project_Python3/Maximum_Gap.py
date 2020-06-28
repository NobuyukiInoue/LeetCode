# coding: utf-8

import os
import sys
import time
from functools import lru_cache

class Solution:
#   def maximumGap(self, nums: List[int]) -> int:
    def maximumGap(self, nums):
        # 48ms
        nums.sort()
        maxGap = 0
        for i in range(len(nums) - 1):
            temp = nums[i + 1] - nums[i]
            if temp > maxGap:
                maxGap = temp
        return maxGap

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip().split(",")
    nums = [int(n) for n in flds]
    print("nums = {0}".format(nums))

    sl = Solution()
    time0 = time.time()
    result = sl.maximumGap(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
