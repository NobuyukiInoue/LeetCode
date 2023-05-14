# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # 43ms - 47ms
        while part in s:
            s = s.replace(part, "", 1)
        return s

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
    flds = temp.replace(", ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    s, part = flds[0], flds[1]
    print("s = \"{0}\", part = \"{1}\"".format(s, part))

    sl = Solution()
    time0 = time.time()

    result = sl.removeOccurrences(s, part)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
