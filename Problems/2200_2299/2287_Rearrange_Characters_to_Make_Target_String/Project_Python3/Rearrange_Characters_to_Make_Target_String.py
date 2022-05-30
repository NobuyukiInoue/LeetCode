# coding: utf-8

import collections
import os
import sys
import time
from typing import Collection, List, Dict, Tuple

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        # 31ms - 58ms
        cnt1, cnt2 = map(collections.Counter, (s, target))
        return min(cnt1[c] // cnt2[c] for c in cnt2)

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
    flds = temp.replace(" ","").replace("\"","").replace("[","").replace("]","").rstrip()

    clocks = flds.split(",")
    s, target = clocks[0], clocks[1]
    print("s = {0}, target = {1}".format(s, target))
  
    sl = Solution()
    time0 = time.time()

    result = sl.rearrangeCharacters(s, target)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
