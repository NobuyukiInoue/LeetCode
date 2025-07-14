import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maxDifference(self, s: str) -> int:
        # 0ms - 3ms
        cnts = collections.Counter(s)
        max_odd = max(x for x in cnts.values() if x % 2 == 1)
        min_even = min(x for x in cnts.values() if x % 2 == 0)
        return max_odd - min_even

    def maxDifference1(self, s: str) -> int:
        # 1ms - 3ms
        cnts = list(collections.Counter(s).values())
        max_odd, min_even = 1, len(s)
        for cnt in cnts:
            if cnt%2 == 1:
                max_odd = max(max_odd, cnt)
            else:
                min_even = min(min_even, cnt)
        return max_odd - min_even

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
    s = temp.replace("\"", "").replace("[", "").replace("]", "").rstrip()
    print("s = \"{0}\"".format(s))

    sl = Solution()
    time0 = time.time()

    result = sl.maxDifference(s)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
