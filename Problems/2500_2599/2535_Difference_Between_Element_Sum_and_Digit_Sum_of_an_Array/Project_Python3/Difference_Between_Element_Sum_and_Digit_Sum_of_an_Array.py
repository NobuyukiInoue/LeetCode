# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        # 128ms - 132ms
        ele, dig = 0, 0
        for num in nums:
            ele += num
            if num >= 10:
                while num > 0:
                    dig += num % 10
                    num //= 10
            else:
                dig += num
        return ele - dig

    def differenceOfSum_2liner(self, nums: List[int]) -> int:
        # 142ms - 143ms
        digitSum = sum((map(int,list(''.join(map(str,nums))))))
        return sum(nums) - digitSum

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

    result = sl.differenceOfSum(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
