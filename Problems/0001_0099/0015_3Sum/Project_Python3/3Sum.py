# coding: utf-8

import os
import sys
import time
import numpy as np

class Solution:
    def threeSum(self, nums):     
        nums.sort()
        res = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: continue
            l, r = i+1, len(nums)-1
            
            while l < r:
                s = nums[l] + nums[i] + nums[r]
                if   s > 0: r -= 1
                elif s < 0: l += 1
                else:
                    res.append((nums[l],nums[i],nums[r]))
                    while l < r and nums[l] == nums[l+1]: l += 1
                    while l < r and nums[r] == nums[r-1]: r -= 1
                    l, r = l+1, r-1
        return res

    def threeSum_work(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j + 1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp_arr = [nums[i], nums[j], nums[k]]
                        temp_arr.sort()
                        results.append(temp_arr)    
        return results

def main():
    argv = sys.argv
    argc = len(argv)

    if (argc < 2):
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
    flds = temp.replace("[","").replace("]","").rstrip().split(",")

    nums = [int(val) for val in flds]
    print("nums = %s" %nums)

    time0 = time.time()

    sl = Solution()
    result = sl.threeSum(nums)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
