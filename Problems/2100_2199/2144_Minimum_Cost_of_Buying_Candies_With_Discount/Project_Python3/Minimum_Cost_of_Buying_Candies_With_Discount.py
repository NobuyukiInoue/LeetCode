# coding: utf-8

import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # 48ms
        return sum(_ for i, _ in enumerate(sorted(cost)) if (len(cost) - i) % 3)

    def minimumCost2(self, cost: List[int]) -> int:
        # 82ms
        cost.sort(reverse=True)
        free = [cost[i] for i in range(2, len(cost)) if (i + 1)% 3 == 0]
        return sum(cost) - sum(free)

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

    cost = [int(n) for n in flds.split(",")]
    print("cost = {0}".format(cost))

    sl = Solution()

    time0 = time.time()

    result = sl.minimumCost(cost)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
