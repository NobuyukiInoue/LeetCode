import collections
import os
import sys
import time
import re
from typing import List, Dict, Tuple

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 108ms
        need, missing = collections.Counter(t), len(t)
        i, i2, j2 = 0, 0, 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not j2 or j - i <= j2 - i2:
                    i2, j2 = i, j
        return s[i2:j2]

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
    flds = temp.replace(", ", ",").replace("\"","").replace("[","").replace("]","").rstrip().split(",")
    s, t = flds[0], flds[1]

    print("s = {0}, t = {1}".format(s, t))

    sl = Solution()
    time0 = time.time()

    result = sl.minWindow(s, t)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
