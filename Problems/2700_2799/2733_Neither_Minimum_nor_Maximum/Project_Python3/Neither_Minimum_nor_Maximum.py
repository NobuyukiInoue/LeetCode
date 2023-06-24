import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        # 386ms - 432m
        nums.sort()
        if (len(nums)-2) <= 0:
            return -1
        return nums[1]

    def findNonMinOrMax2(self, nums: List[int]) -> int:
        # 394ms - 446ms
        mi, ma = min(nums), max(nums)
        for _, num in enumerate(nums):
            if num != mi and num != ma:
                return num
        return -1

    def findNonMinOrMax3(self, nums: List[int]) -> int:
        # 465ms - 506ms
        if len(nums) < 3:
            return -1
        mi, ma = sys.maxsize, -1
        for _, num in enumerate(nums):
            mi = min(mi, num)
            ma = max(ma, num)
        for _, num in enumerate(nums):
            if num != mi and num != ma:
                return num
        return -1

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

    result = sl.findNonMinOrMax(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
