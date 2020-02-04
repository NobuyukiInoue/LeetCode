# coding: utf-8

import itertools
import os
import sys
import time

from functools import reduce


class Solution:
#   def permuteUnique(self, nums: List[int]) -> List[List[int]]:    
    def permuteUnique(self, nums):
        # 52ms
        nums.sort()
        res = []
        def helper(nums, cur, n):
            if len(cur) == n:
                res.append(cur)
                return 
            for i in range(len(nums)):
                if i > 0 and nums[i-1] == nums[i]:
                    continue
                helper(nums[:i] + nums[i+1:], cur + [nums[i]], n)
        helper(nums, [], len(nums))
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

    time0 = time.time()

    sl = Solution()
    result = sl.permuteUnique(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
