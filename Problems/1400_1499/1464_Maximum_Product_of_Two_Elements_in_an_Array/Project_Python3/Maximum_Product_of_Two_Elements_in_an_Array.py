# coding: utf-8

import os
import sys
import time
import math

class Solution:
#   def maxProduct(self, nums: List[int]) -> int:
    def maxProduct(self, nums):
        # 40ms
        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)

    def maxProduct2(self, nums):
        # 52ms
        m = n = -math.inf
        for num in nums:
            if num >= m:
                n = m
                m = num
            elif num > n:
                n = num
        return (m - 1) * (n - 1)

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    nums = [int(n) for n in flds.split(",")]
    print("nums = {0}".format(nums))

    sl = Solution()

    time0 = time.time()

    result = sl.maxProduct(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
