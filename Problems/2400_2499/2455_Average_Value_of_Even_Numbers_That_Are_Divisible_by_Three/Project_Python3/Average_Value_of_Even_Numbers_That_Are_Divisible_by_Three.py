# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        # 85ms - 156ms 
        nums = [n for n in nums if not n%6]
        return sum(nums)//len(nums) if nums else 0

    def averageValue2(self, nums: List[int]) -> int:
        # 149ms - 216ms
        cnt, total = 0, 0
        for num in nums:
            if num % 2 == 0 and num % 3 == 0:
                total += num
                cnt += 1
        if cnt > 0:
            return total // cnt
        return 0

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

    result = sl.averageValue(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
