# coding: utf-8

import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 52ms
        if not nums:
            return 0
        memory = set(nums)
        current_max = 1
        for num in nums:
            if num - 1 in memory:
                continue
            counter = 1
            while num + 1 in memory:
                counter += 1
                num += 1
            current_max = max(current_max, counter)
        return current_max

    def longestConsecutive2(self, nums: List[int]) -> int:
        # 56ms
        nums.sort()
        if len(nums) == 1:
            return 1
        current, current_max = 1, 0
        for i in range(len(nums) - 1):
            if nums[i + 1]  == nums[i] + 1:
                current += 1
            elif nums[i + 1] == nums[i]:
                pass
            else:
                current = 1
            current_max = max(current, current_max)
        return current_max

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

    result = sl.longestConsecutive(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
