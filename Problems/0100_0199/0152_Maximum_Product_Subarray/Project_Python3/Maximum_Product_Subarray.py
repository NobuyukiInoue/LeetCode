# coding: utf-8

import collections
import os
import sys
import time

class Solution:
#   def maxProduct(self, nums: List[int]) -> int:
    def maxProduct(self, nums):
        # 60ms
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        maxP = [0]*len(nums)
        minP = [0]*len(nums)
        maxP[0], minP[0], res = nums[0], nums[0], nums[0]
        for i in range(len(nums)):
            maxP[i] = max(max(maxP[i - 1]*nums[i], minP[i - 1]*nums[i]), nums[i])
            minP[i] = min(min(maxP[i - 1]*nums[i], minP[i - 1]*nums[i]), nums[i])
            res = max(res, maxP[i])
        return res

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python %s <testdata.txt>" %(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("%s not found..." %argv[1])
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip().split(",")
    nums = [int(n) for n in flds]
    print("nums = {0}".format(nums))

    time0 = time.time()

    sl = Solution()
    result = sl.maxProduct(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
