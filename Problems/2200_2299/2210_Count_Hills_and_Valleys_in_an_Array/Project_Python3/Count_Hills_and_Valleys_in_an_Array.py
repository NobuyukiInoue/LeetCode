# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # 52ms
        res, i  = 0, 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                i += 1
                continue
            dirrection = (nums[i] < nums[i + 1])
            i += 1
            break
        while i < len(nums) - 1:
            if dirrection:
                if nums[i] > nums[i + 1]:
                    dirrection = False
                    res += 1
            else:
                if nums[i] < nums[i + 1]:
                    dirrection = True
                    res += 1
            i += 1
        return res

    def countHillValley2(self, nums: List[int]) -> int:
        # 69ms
        count, last = 0, nums[0]
        for i in range(1, len(nums)-1):
            last = nums[i - 1] if nums[i] != nums[i - 1] else last
            count += 1 if (last < nums[i] > nums[i + 1] or last > nums[i] < nums[i + 1]) else 0
        return count


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
    flds = temp.replace("[","").replace("]","").replace(", ",",").rstrip()
    nums = [int(n) for n in flds.split(",")]
    print("nums = {0}".format(nums))

    sl = Solution()

    time0 = time.time()

    result = sl.countHillValley(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
