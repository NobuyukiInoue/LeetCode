# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def captureForts(self, forts: List[int]) -> int:
        # 34ms - 48ms
        current_idx, max_forts = 0, 0
        for i, fort in enumerate(forts):
            if fort != 0:
                if forts[current_idx] == -fort:
                    max_forts = max(max_forts, i - current_idx - 1)
                current_idx = i
        return max_forts

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
    forts = [int(n) for n in flds.split(",")]
    print("forts = {0}".format(forts))

    sl = Solution()

    time0 = time.time()

    result = sl.captureForts(forts)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
