# coding: utf-8

import collections
import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        res = [0]*(2051 - 1950)
        for i, j in logs:
            for k in range(i - 1950, j - 1950):
                res[k] += 1
        return res.index(max(res)) + 1950

    def maximumPopulation2(self, logs: List[List[int]]) -> int:
        # 40ms
        dic = collections.defaultdict(int)
        for y_b, y_d in logs:
            for y in range(y_b, y_d):
                dic[y] += 1
        return max(dic.items(), key=lambda x: (x[1], -x[0]))[0]

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

    logs = [[int(n) for n in fld.split(",")] for fld in flds]
    print("logs = {0}".format(logs))

    sl = Solution()

    time0 = time.time()

    result = sl.maximumPopulation(logs)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
