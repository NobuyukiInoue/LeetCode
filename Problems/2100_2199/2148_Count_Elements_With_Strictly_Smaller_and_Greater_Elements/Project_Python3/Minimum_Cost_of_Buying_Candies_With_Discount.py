# coding: utf-8

import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def countElements(self, nums: List[int]) -> int:
        # 44ms
        nums.sort()
        res = 0
        for _, num in enumerate(nums):
            if nums[0] < num and num < nums[-1]:
                res += 1
        return res

    def countElements_min_max(self, nums: List[int]) -> int:
        # 67ms
        v_min = min(nums)
        v_max = max(nums)
        res = 0
        for _, num in enumerate(nums):
            if num > v_min and num < v_max:
                res += 1
        return res

    def countElements_twoliner(self, nums: List[int]) -> int:
        # 63ms
        count = collections.Counter(nums)
        return 0 if len(count) < 3 else len(nums) - count[min(count)] - count[max(count)]


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

    result = sl.countElements(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
