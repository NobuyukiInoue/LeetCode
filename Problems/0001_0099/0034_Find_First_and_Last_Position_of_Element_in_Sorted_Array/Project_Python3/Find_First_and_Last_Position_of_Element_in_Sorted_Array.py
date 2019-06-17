# coding: utf-8

import os
import sys
import time

class Solution:
#   def searchRange(self, nums: List[int], target: int) -> List[int]:
    def searchRange(self, nums, target):
        # 40ms
        hit, low, high = False, float('inf'), 0
        for i in nums:
            if i == target:
                hit = True
        if not hit:
            return [-1, -1]
        for i in range(0, len(nums)):
            if nums[i] == target:
                if i > high:
                    high = i
                if i < low:
                    low = i
        return [low, high]

    def searchRange2(self, nums, target):
        # 44ms
        if nums == []:
           return [-1, -1]
        l, r = 0, len(nums) - 1
        if nums[l] == target and nums[r] == target:
            return [l, r]
        while l <= r:
            if nums[l] == target and nums[r] == target:
                return [l, r]
            else:
                if nums[r] > target:
                    r -= 1
                elif nums[l] < target:
                    l += 1
                else:
                    return [l, r]
        return [-1, -1]

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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")

    nums = [int(n) for n in flds[0].split(",")]
    target = int(flds[1])
    print("nums = %s, target = %d" %(nums, target))

    time0 = time.time()

    sl = Solution()
    result = sl.searchRange(nums, target)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
