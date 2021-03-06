# coding: utf-8

import heapq
import os
import sys
import time

class Solution:
#    def distributeCandies(self, candies: List[int]) -> int:
    def findUnsortedSubarray(self, nums):
        x = sorted(nums)
        l = len(nums)
        if nums == x:
            return 0
        lindex, rindex = 0, 0
        for i in range(l):
            if nums[i] != x[i]:
                lindex = i
                break
        for i in range(l):
            if nums[l - 1 - i] != x[l - 1 - i]:
                rindex = l-i
                break
        return rindex - lindex

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
    flds = temp.replace(" ","").replace("[","").replace("]","").rstrip()

    nums = [int(n) for n in flds.split(",")]
    print("nums = {0}".format(nums))

    sl = Solution()
    time0 = time.time()
    result = sl.findUnsortedSubarray(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
