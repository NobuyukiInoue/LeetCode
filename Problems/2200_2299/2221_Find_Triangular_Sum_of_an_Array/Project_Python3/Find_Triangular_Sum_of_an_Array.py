# coding: utf-8

import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        # 143ms - 160ms
        res, nCr, n = 0, 1, len(nums) - 1
        for r, num in enumerate(nums):
            res = (res + num*nCr) % 10
            nCr = nCr*(n - r) // (r + 1)
        return res

    def triangularSum_while1(self, nums: List[int]) -> int:
        # 2300ms - 2306ms
        return nums[0] if len(nums) == 1 else self.triangularSum([(nums[i] + nums[i+1]) % 10 for i in range(len(nums) - 1)])

    def triangularSum_while2(self, nums: List[int]) -> int:
        # 2682ms - 2705ms
        while len(nums) > 1:
            temp = []
            for i in range(len(nums) - 1):
                temp.append((nums[i] + nums[i + 1])%10)
            nums = temp
        return nums[0]

    def triangularSum_comb1(self, nums: List[int]) -> int:
        # 2796ms - 2801ms
        return sum(n * math.comb(len(nums) - 1, i) for i, n in enumerate(nums)) % 10

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

    result = sl.triangularSum(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
