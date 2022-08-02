# coding: utf-8

import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        # 37ms - 43ms
        cnts = collections.Counter(nums).values()
        return [sum(v // 2 for v in cnts), sum(v % 2 for v in cnts)]

    def numberOfPairs2(self, nums: List[int]) -> List[int]:
        # 60ms - 68ms
        nums.sort()
        count, i = 0, 1
        while i < (len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
                i += 1
            i += 1
        return (count, len(nums)-count*2)

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

    result = sl.numberOfPairs(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
