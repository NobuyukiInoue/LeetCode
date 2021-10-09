# coding: utf-8

import collections
import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # 24ms
        s = list(map(int, str(n)))
        i = len(s) - 1
        while i - 1 >= 0 and s[i] <= s[i - 1]:
            i -= 1
        if i == 0:
            return -1
        j = i
        while j + 1 < len(s) and s[j + 1] > s[i - 1]:
            j += 1
        s[i - 1], s[j] = s[j], s[i - 1]
        s[i:] = reversed(s[i:])
        ans = int("".join(map(str, s)))
        return ans if ans <=((1<<31) - 1) else -1

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

    n = int(flds)
    print("n = {0:d}".format(n))

    sl = Solution()

    time0 = time.time()

    result = sl.nextGreaterElement(n)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
