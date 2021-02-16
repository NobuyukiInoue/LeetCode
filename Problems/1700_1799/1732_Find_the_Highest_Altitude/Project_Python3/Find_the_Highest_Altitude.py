# coding: utf-8

import itertools
import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # 28ms
        return max(0, max(itertools.accumulate(gain)))

    def largestAltitude2(self, gain: List[int]) -> int:
        # 36ms
        height, heightMax = 0, 0
        for n in gain:
            height += n
            if height > heightMax:
                heightMax = height
        return heightMax

    def largestAltitude3(self, gain: List[int]) -> int:
        # 36ms
        if not gain:
            return 0
        gain = [0] + gain
        for i in range(1, len(gain)):
            gain[i] += gain[i - 1]
        return max(gain)

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

    gain = [int(n) for n in flds.split(",")]
    print("gain = {0}".format(gain))

    sl = Solution()

    time0 = time.time()

    result = sl.largestAltitude(gain)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
