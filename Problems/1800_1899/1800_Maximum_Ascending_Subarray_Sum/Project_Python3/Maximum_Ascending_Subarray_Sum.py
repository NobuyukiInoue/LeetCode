# coding: utf-8

import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # 28ms
        currentSum = maxSum = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                currentSum += nums[i]
                if currentSum > maxSum:
                    maxSum = currentSum
            else:
                currentSum = nums[i]
        return maxSum

    def maxAscendingSum2(self, nums: List[int]) -> int:
        # 264ms
        return max([sum(nums[i:j]) for j in range(len(nums)+1) for i in range(len(nums)) if nums[i:j] == sorted(set(nums[i:j]))])

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

    result = sl.maxAscendingSum(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
