# coding: utf-8

import os
import sys
import time
import math

class Solution:
#   def sortColors(self, nums: List[int]) -> None:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # 32ms
        red, white, blue = 0, 0, 0
        for n in nums:
            if n == 0:
                red += 1
            elif n == 1:
                white += 1
            else:
                blue += 1
        i = 0
        for n in range(red):
            nums[i] = 0
            i += 1
        for n in range(white):
            nums[i] = 1
            i += 1
        for n in range(blue):
            nums[i] = 2
            i += 1

    def sortColors2(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # 36ms
        red, white, blue = [], [], []
        for n in nums:
            if n == 0:
                red.append(n)
            elif n == 1:
                white.append(n)
            else:
                blue.append(n)
        i = 0
        for n in red:
            nums[i] = n
            i += 1
        for n in white:
            nums[i] = n
            i += 1
        for n in blue:
            nums[i] = n
            i += 1

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

    sl.sortColors(nums)

    time1 = time.time()

    print("result = {0}".format(nums))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
