# coding: utf-8

import collections
import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # 56ms
        numof = collections.Counter(sorted(digits))
        evens = [digit for digit in numof if not digit&1]
        hundreds = [digit for digit in numof if digit > 0]
        return([100*a + 10*b + c for a in hundreds for b in numof for c in evens 
            if 
            (numof[a] > (a == b) + (a == c)) and
            (numof[b] > (b == a) + (b == c)) and
            (numof[c] > (c == a) + (c == b))])

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
    flds = temp.replace("[", "").replace("]", "").replace(", ", ",").rstrip()

    digits = [int(n) for n in flds.split(",")]
    print("digits = {0}".format(digits))

    sl = Solution()

    time0 = time.time()

    result = sl.findEvenNumbers(digits)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
