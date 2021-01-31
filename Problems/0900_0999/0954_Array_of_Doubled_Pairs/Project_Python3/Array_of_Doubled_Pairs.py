# coding: utf-8

import collections
import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        # 552ms
        dic = collections.Counter(arr)
        keys = list(dic.keys())
        keys.sort()
        for k in keys:
            if dic[k] != 0 and 2*k in dic:
                if dic[k] > dic[k*2]:
                    dic[k] -= dic[k*2]
                    dic[k*2] = 0
                else:
                    dic[2*k] -= dic[k]
                    dic[k] = 0
        return all( v == 0 for v in dic.values())

    def canReorderDoubled(self, arr: List[int]) -> bool:
        # 736ms
        dic = {}
        for a in arr:
            if a in dic:
                dic[a]  += 1
            else:
                dic[a] = 1
        keys = list(dic.keys())
        keys.sort()
        for k in keys:
            if dic[k] != 0 and 2*k in dic:
                if dic[k] > dic[k*2]:
                    dic[k] -= dic[k*2]
                    dic[k*2] = 0
                else:
                    dic[2*k] -= dic[k]
                    dic[k] = 0
        return all( v == 0 for v in dic.values())


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

    arr = [int(n) for n in flds.split(",")]
    print("arr = {0}".format(arr))

    sl = Solution()

    time0 = time.time()

    result = sl.canReorderDoubled(arr)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
