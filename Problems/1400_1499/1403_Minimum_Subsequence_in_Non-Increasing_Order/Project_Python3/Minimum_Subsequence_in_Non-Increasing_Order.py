# coding: utf-8

import collections
import os
import sys
import time

class Solution:
#   def minSubsequence(self, nums: List[int]) -> List[int]:

    def minSubsequence(self, nums):
        # 52ms, 60ms, 68ms
        if len(nums) <= 1:
            return nums
        nums.sort(reverse = True)
        sum_left, sum_right = 0, sum(nums)
        i = 0
        while sum_left <= sum_right:
            sum_left += nums[i]
            sum_right -= nums[i]
            i += 1
        return nums[:i]

    def minSubsequence2(self, nums):
        # 56ms, 64ms
        sum_left, sum_right = 0, sum(nums)
        nums.sort(reverse = True)
        for i in range(len(nums)):
            sum_left += nums[i]
            sum_right -= nums[i]
            if sum_left > sum_right:
                return nums[:i + 1]

    def minSubsequence3(self, nums):
        # 56ms
        sum_left, sum_right = 0, sum(nums)
        nums.sort()
        for i in range(len(nums) - 1, -1, -1):
            sum_left += nums[i]
            sum_right -= nums[i]
            if sum_left > sum_right:
                return sorted(nums[i:], reverse=True)

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
    result = sl.minSubsequence(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
