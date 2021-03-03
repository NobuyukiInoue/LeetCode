# coding: utf-8

import bisect
import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # 28ms
        digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        seq_nums = []
        for l in range(1, 10):
            for ind in range(len(digits) - l + 1):
                seq_nums.append(digits[ind:ind + l])
        seq_nums = [''.join(num) for num in seq_nums]
        seq_nums = [int(num) for num in seq_nums]
        import bisect
        l = bisect.bisect_left(seq_nums, low)
        r = bisect.bisect_right(seq_nums, high)
        return seq_nums[l:r]

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
    flds = temp.replace("[[","").replace("]]","").replace(", ",",").rstrip().split("],[")

    low, high = int(flds[0]), int(flds[1])
    print("low = {0:d}, high = {1:d}".format(low, high))

    sl = Solution()

    time0 = time.time()

    result = sl.sequentialDigits(low, high)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
