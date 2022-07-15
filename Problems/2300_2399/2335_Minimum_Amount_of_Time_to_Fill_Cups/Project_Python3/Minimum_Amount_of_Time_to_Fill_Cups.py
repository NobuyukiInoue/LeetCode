# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        # 43ms - 49ms
        return max(max(amount), (sum(amount) + 1) // 2)

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
    amount = [int(n) for n in flds.split(",")]
    print("amount = {0}".format(amount))

    sl = Solution()

    time0 = time.time()

    result = sl.fillCups(amount)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
