# coding: utf-8

import collections
import itertools
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        # 104ms - 143ms
        res = 0
        n = len(nums)
        count = collections.defaultdict(lambda: 0)
        count[nums[n - 1] - nums[n - 2]] = 1
        for b in range(n - 3, 0, -1):
            for a in range(b - 1, -1, -1):
                res += count[nums[a] + nums[b]]
            for x in range(n - 1, b, -1):
                count[nums[x] - nums[b]] += 1
        return res

    def countQuadruplets_3loop(self, nums: List[int]) -> int:
        # 410ms - 584ms
        n = len(nums)
        res = 0
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                for k in range(j + 1, n - 1):
                    if nums[i] + nums[j] + nums[k] in nums[k:]:
                        res += nums[k:].count(nums[i] + nums[j] + nums[k])
        return res

    def countQuadruplets_4liner(self, nums: List[int]) -> int:
        # 1296ms - 1393ms
        ans = 0
        for a, b, c, d in itertools.combinations(nums, 4):
            if a + b + c == d:
                ans +=1
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

    result = sl.countQuadruplets(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
