# coding: utf-8

import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # 60ms
        v_max, v_min = max(nums), min(nums)
        for i in range(v_min, 0, -1):
            if v_min%i == 0 and v_max%i == 0:
                return i

    def findGCD1(self, nums: List[int]) -> int:
        # 62ms
        v_max, v_min = max(nums), min(nums)
        while v_min:
            v_max, v_min = v_min, v_max % v_min
        return v_max

    def findGCD2(self, nums: List[int]) -> int:
        # 79ms
        v_min, v_max = nums[0], nums[0]
        for _, n in enumerate(nums):
            v_min = min(v_min, n)
            v_max = max(v_max, n)
        ans = 1
        if v_min == v_max:
            return v_min
        for i in range(1, v_max//2 + 1):
            if v_max % i == 0 and v_min % i == 0:
                ans = i
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

    result = sl.findGCD(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
