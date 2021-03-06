# coding: utf-8

import os
import sys
import time
import numpy as np

class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        results = []
        self.findNsum(nums, target, 4, [], results)
        return results

    def findNsum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2: return

        # solve 2-sum
        if N == 2:
            l, r = 0, len(nums)-1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums) - N + 1):   # careful about range
                if target < nums[i]*N or target > nums[-1]*N:  # take advantages of sorted list
                    break
                if i == 0 or i > 0 and nums[i - 1] != nums[i]:  # recursively reduce N
                    self.findNsum(nums[i + 1:], target-nums[i], N - 1, result+[nums[i]], results)
        return

    def fourSum_work(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if target >= 0:
                if nums[i] > target:
                    break
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j + 1, len(nums) - 1):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    for l in range(k + 1, len(nums)):
                        if l > k + 1 and nums[l] == nums[l - 1]:
                            continue
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            temp_arr = [nums[i], nums[j], nums[k], nums[l]]
                            temp_arr.sort()
                            results.append(temp_arr)
        return results

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
    flds = temp.replace(" ","").replace("[[","").replace("]]","").rstrip().split("],[")

    nums = [int(val) for val in flds[0].split(",")]
    target = int(flds[1])

    print("nums = {0}".format(nums))
    print("target = {0}".format(target)
)
    sl = Solution()
    time0 = time.time()

    result = sl.fourSum(nums, target)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
