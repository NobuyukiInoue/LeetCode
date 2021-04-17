import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def secondHighest(self, s: str) -> int:
        # 24ms
        return -1 if len(sorted([x for x in set(s) if x.isdigit()])) < 2 else sorted([x for x in set(s) if x.isdigit()])[-2]

    def secondHighest2(self, s: str) -> int:
        # 36ms
        firstLagest, secondLagest = -1, -1
        for ch in s:
            if ch.isnumeric():
                ch_val = int(ch)
                if 0 <= ch_val <= 9:
                    if ch_val > firstLagest:
                        secondLagest = firstLagest
                        firstLagest = ch_val
                    elif ch_val > secondLagest and ch_val < firstLagest:
                        secondLagest = ch_val
        return secondLagest

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
    s = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("s = {0}".format(s))

    sl = Solution()
    time0 = time.time()

    result = sl.secondHighest(s)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
