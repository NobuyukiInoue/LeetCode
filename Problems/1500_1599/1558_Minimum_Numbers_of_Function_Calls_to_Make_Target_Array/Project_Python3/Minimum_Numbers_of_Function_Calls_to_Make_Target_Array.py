# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    """
    def modify(self, arr: List[int], op: int, idx: int) -> None:
        # add by 1 index idx
        if op == 0:
            arr[idx] += 1
        # multiply by 2 all elements
        if op == 1:
            for i, _ in enumerate(arr):
                arr[i] *= 2
    """

    def minOperations(self, nums: List[int]) -> int:
        # 818ms - 1140ms
        cnt_add, cnt_dbl, tmp = 0, 0, 0
        for _, num in enumerate(nums):
            if num != 0:
                cnt_add += 1
            tmp = 0
            while num > 1:
                if num % 2 == 1:
                    cnt_add += 1
                tmp += 1
                num >>= 1
            cnt_dbl = max(tmp, cnt_dbl)
        return cnt_dbl + cnt_add

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

    result = sl.minOperations(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
