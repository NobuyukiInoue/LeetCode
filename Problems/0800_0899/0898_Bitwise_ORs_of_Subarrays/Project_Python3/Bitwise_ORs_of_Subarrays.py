# coding: utf-8

import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        # 752ms
        result = set(arr)
        stor = arr
        while stor:
            stor = [i | j for i, j in zip(stor, stor[1:])]
            stor = [i for i, j in zip(stor, stor[1:] + [-1]) if i != j]
            result.update(stor)
        return len(result)

    def subarrayBitwiseORs2(self, arr: List[int]) -> int:
        # 772ms
        res, cur = set(), set()
        for i in arr:
            cur = {i | j for j in cur} | {i}
            res |= cur
        return len(res)

    def subarrayBitwiseORs3(self, arr: List[int]) -> int:
        # 948ms
        hash, curr = {}, {}
        for _, v in enumerate(arr):
            next = {}
            for _, k in enumerate(curr):
                next[k|v] = 0
                hash[k|v] = 0
            next[v] = 0
            hash[v] = 0
            curr = next
        return len(hash)

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    nums = [int(n) for n in flds.split(",")]
    print("nums = {0}".format(nums))

    sl = Solution()

    time0 = time.time()

    result = sl.subarrayBitwiseORs(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
