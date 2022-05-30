# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        # 31ms - 41ms
        cnt = 0
        for _, ch in enumerate(s):
            if ch == letter:
                cnt += 1
        return 100*cnt//len(s)

    def percentageLetter_1liner(self, s: str, letter: str) -> int:
        # 51ms - 79ms
        return 100*s.count(letter)//len(s)

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
    s, letter = clocks[0], clocks[1]
    print("s = {0}, letter = {1}".format(s, letter))
  
    sl = Solution()
    time0 = time.time()

    result = sl.percentageLetter(s, letter)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
