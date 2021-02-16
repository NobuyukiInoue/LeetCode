# coding: utf-8

import itertools
import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # 216ms
        return list(itertools.accumulate([first] + encoded, lambda x, y: x ^ y))

    def decode3(self, encoded: List[int], first: int) -> List[int]:
        # 216ms
        res = [first]
        for v in encoded:
            res.append(v^res[-1])
        return res

    def decode3(self, encoded: List[int], first: int) -> List[int]:
        # 220ms
        res = [first]
        for i, v in enumerate(encoded):
            res.append(v^res[i])
        return res

    def decode4(self, encoded: List[int], first: int) -> List[int]:
        # 228ms
        res = [0]*(len(encoded) + 1)
        res[0] = first
        for i, v in enumerate(encoded):
            res[i + 1] = v^res[i]
        return res

    def decode5(self, encoded: List[int], first: int) -> List[int]:
        # 308ms
        res = [0]*(len(encoded) + 1)
        res[0] = first
        for i in range(len(encoded)):
            res[i + 1] = encoded[i]^res[i]
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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")
    encoded = [int(n) for n in flds[0].split(",")]
    first = int(flds[1])
    print("encoded = {0}, first = {1:d}".format(encoded, first))

    sl = Solution()

    time0 = time.time()

    result = sl.decode(encoded, first)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
