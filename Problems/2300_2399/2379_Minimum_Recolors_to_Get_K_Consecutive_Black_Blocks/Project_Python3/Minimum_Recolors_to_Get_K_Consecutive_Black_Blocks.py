# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # 39ms - 54ms
        lo, white, mi = -1, 0, sys.maxsize
        for hi, c in enumerate(blocks):
            if c == 'W':
                white += 1
            if hi - lo >= k:
                mi = min(white, mi)
                lo += 1
                white -= blocks[lo] == 'W' 
        return mi

    def minimumRecolors_4liner(self, blocks: str, k: int) -> int:
        # 50ms - 63ms
        res = sys.maxsize
        for i in range(len(blocks)- k + 1):
            res = min(res, blocks.count('W', i, i + k))
        return res


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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    blocks = flds[0]
    k = int(flds[1])
    print("blocks = {0}, k = {1:d}".format(blocks, k))

    sl = Solution()
    time0 = time.time()

    result = sl.minimumRecolors(blocks, k)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
