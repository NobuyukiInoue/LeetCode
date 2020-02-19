# coding: utf-8

import collections
import os
import sys
import time

class Solution:
#   def findDuplicate(self, nums: List[int]) -> int:
    def findDuplicate(self, nums):
        # 64ms
        slow, fast = 0, 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

    def findDuplicate2(self, nums):
        # 88ms
        left, right = 1, len(nums)-1
        while left < right:
            mid = (right + left)//2
            if sum(i <= mid for i in nums) > mid:
                left, right = [left, mid]
            else:
                left, right = [mid + 1, right]
        return right

    def findDuplicate3(self, nums):
        # Time Limit Exceeded
        nums_len = len(nums)
        for i in range(nums_len):
            for j in range(i + 1, nums_len):
                if nums[i] == nums[j]:
                    return nums[i]
        return -1

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    nums = [int(n) for n in flds.split(",")]
    print("nums = {0}".format(nums))

    time0 = time.time()

    sl = Solution()
    result = sl.findDuplicate(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
