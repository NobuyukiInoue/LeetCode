# coding: utf-8

import functools
import operator
import itertools
import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # 32ms
        return functools.reduce(operator.or_, nums, 0) * 2**(len(nums) - 1)

    def subsetXORSum2(self, nums: List[int]) -> int:
        # 44ms
        result = 0
        subsets = [0]
        for n in nums:
            new_subsets = subsets.copy()
            for s in subsets:
                new_subsets.append(s ^ n)
                result += new_subsets[-1]
            subsets = new_subsets
        return result

    def subsetXORSum3(self, nums: List[int]) -> int:
        # 64ms
        def sums(term, idx):
            if idx == len(nums):
                return term            
            return sums(term, idx + 1) + sums(term ^ nums[idx], idx + 1)
        return sums(0, 0)

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

    result = sl.subsetXORSum(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
