# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # 36ms - 60ms
        return bin(start^goal).count("1")

    def minBitFlips2(self, start: int, goal: int) -> int:
        # 41ms - 56ms
        return (start^goal).bit_count()

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
    start, goal = nums[0], nums[1]
    print("start = {0:d}, goal = {1:d}".format(start, goal))

    sl = Solution()

    time0 = time.time()

    result = sl.minBitFlips(start, goal)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
