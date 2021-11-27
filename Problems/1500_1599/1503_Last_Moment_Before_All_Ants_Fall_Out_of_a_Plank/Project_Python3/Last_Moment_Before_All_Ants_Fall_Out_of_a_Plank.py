# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        # 152ms
        return max(max(left, default = -1), n - min(right, default = n))


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
    flds = temp.replace(" ", "").replace("\"", "").replace("[[", "").replace("]]", "").rstrip().split("],[")

    n = int(flds[0])
    left = [int(_) for _ in flds[1].split(",")] if len(flds[1]) > 0 else []
    right = [int(_) for _ in flds[2].split(",")] if len(flds[2]) > 0 else []

    print("n = {0}, left = {1}, right = {2}".format(n, left, right))

    sl = Solution()
    time0 = time.time()

    result = sl.getLastMoment(n, left, right)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
