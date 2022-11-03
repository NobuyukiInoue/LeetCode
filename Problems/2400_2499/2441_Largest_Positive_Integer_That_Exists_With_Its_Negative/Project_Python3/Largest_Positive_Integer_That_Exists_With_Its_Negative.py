# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        # 127ms - 329ms
        nums = sorted(nums)
        index = len(nums)-1
        while index > -1:
            num = nums[index]
            if -num in nums:
                return num
            index = index - 1
        return -1

    def findMaxK_for(self, nums: List[int]) -> int:
        # 294ms - 346ms
        nums = sorted(nums)
        for i in range(len(nums) - 1, -1, -1):
            if -nums[i] in nums:
                return nums[i]
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
    nums = [int(n) for n in flds.split(",")]
    print("nums = {0}".format(nums))

    sl = Solution()

    time0 = time.time()

    result = sl.findMaxK(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
