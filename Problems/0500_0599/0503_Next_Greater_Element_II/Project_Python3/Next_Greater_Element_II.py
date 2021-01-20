# coding: utf-8

import copy
import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # 196ms
        numsLen = len(nums)
        res = [-1]*numsLen
        stack = nums[::-1]
        for i in range(numsLen - 1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(nums[i])
        return res

    def nextGreaterElements2(self, nums: List[int]) -> List[int]:
        # 248ms
        numsLen = len(nums)
        for i in range(numsLen - 1):
            nums.append(nums[i])
        res = [-1]*numsLen
        incStack = []
        for i in range(len(nums)):
            element = nums[i]
            while len(incStack) > 0 and nums[incStack[-1]] < element:
                if incStack[-1] < numsLen and res[incStack[-1]] == -1:
                    res[incStack[-1]] = element
                incStack.pop()
            incStack.append(i)
        return res

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

    result = sl.nextGreaterElements(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
