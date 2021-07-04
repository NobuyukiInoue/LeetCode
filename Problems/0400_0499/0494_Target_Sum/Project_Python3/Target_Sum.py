# coding: utf-8

import collections
import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 204ms
        total = 0
        for i, n in enumerate(nums):
            total += n
            nums[i] *= 2
        if abs(total) < abs(target):
            return 0
        target += total
        dp = [0]*(target + 1)
        dp[0] = 1
        for i, _ in enumerate(nums):
            for j in range(target, -1, -1):
                if j >= nums[i]:
                    dp[j] += dp[j-nums[i]]
        return dp[target]

    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        # 304ms
        count = collections.Counter({0: 1})
        for x in nums:
            step = collections.Counter()
            for y in count:
                step[y + x] += count[y]
                step[y - x] += count[y]
            count = step
        return count[target]

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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")
    nums = [int(n) for n in flds[0].split(",")]
    target = int(flds[1])
    print("nums = {0}, target = {1:d}".format(nums, target))

    sl = Solution()

    time0 = time.time()

    result = sl.findTargetSumWays(nums, target)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
