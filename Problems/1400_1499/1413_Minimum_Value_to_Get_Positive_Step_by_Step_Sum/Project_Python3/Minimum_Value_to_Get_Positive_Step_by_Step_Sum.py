# coding: utf-8

import collections
import os
import sys
import time

class Solution:
#   def minStartValue(self, nums: List[int]) -> int:
    def minStartValue(self, nums):
        # 16ms
        total, min_total = 0, sys.maxsize
        for n in nums:
            total += n
            if total < min_total:
                min_total = total
        if -min_total + 1 > 0:
            return -min_total + 1
        return 1

    def minStartValue2(self, nums):
        # 28ms
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]
        return max((1 - min(nums)), 1)
  

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
    result = sl.minStartValue(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
