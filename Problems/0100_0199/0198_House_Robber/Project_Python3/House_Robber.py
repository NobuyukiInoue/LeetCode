# coding: utf-8

import os
import sys
import time

class Solution:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        c = [0] * len(nums)
        c[0] = nums[0]
        c[1] = max(nums[0] ,nums[1])
        for i in range(2, len(nums)):
            c[i] = max(nums[i] + c[i-2], c[i-1])
        return max(c)

def array_str_to_int(numbersStr):
    numbers = [0]*len(numbersStr)
    for i in range(len(numbersStr)):
        numbers[i] = int(numbersStr[i])
    return numbers

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
    numsStr = temp.replace("[","").replace("]","").split(",")
    nums = array_str_to_int(numsStr)

    sl = Solution()
    time0 = time.time()
    result = sl.rob(nums)
    print("result = {0}".format(result))

    time1 = time.time()

    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
