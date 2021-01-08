# coding: utf-8

import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # 64ms
        i = 0
        while i < len(nums) - 1:
            if nums[i] != nums[i + 1]:
                return nums[i]
            i += 2
        return nums[i]

    def singleNonDuplicate_bst(self, nums: List[int]) -> int:
        # 68ms
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if mid % 2:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                start += 2
            else:
                end = mid
        return nums[start]

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
    print("nums   = {0}".format(nums))

    sl = Solution()

    time0 = time.time()

    result = sl.singleNonDuplicate(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
