# coding: utf-8

import os
import sys
import time

class Solution:
#   def firstMissingPositive(self, nums: List[int]) -> int:
    def firstMissingPositive(self, nums):
        # 36ms
        if not nums:
            return 1
        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] > len(nums):
                nums[i] = 0
        nums.sort()
        for i in range(1, len(nums)+2):
            if i not in nums:
                return i

    def firstMissingPositive2(self ,nums):
        # 40ms
        nums_work = list(set(nums))
        nums_work.sort()
        counter = 1
        for n in nums_work:
            if n <= 0:
                continue
            if counter < n:
                return counter
            if n != counter:
                return counter
            counter += 1
        return counter

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip().split(",")
    nums = [int(n) for n in flds]

    sl = Solution()
    time0 = time.time()

    result = sl.firstMissingPositive(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
