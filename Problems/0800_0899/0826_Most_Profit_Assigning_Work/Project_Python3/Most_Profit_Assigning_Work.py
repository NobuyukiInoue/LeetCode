# coding: utf-8

import collections
import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # 332ms
        jobs = sorted(zip(difficulty, profit))
        res = i = best = 0
        for ability in sorted(worker):
            while i < len(jobs) and ability >= jobs[i][0]:
                best = max(jobs[i][1], best)
                i += 1
            res += best
        return res

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # 356ms
        tbl_temp = [(difficulty[i], profit[i]) for i in range(len(difficulty))]
        # print(tbl_temp)
        tbl_temp.sort()
        # print(tbl_temp)
        tbl = [tbl_temp[0]]
        for i in range(1, len(tbl_temp)):
            if tbl_temp[i][1] > tbl_temp[i - 1][1] and tbl_temp[i][1] > tbl[-1][1]:
                tbl.append(tbl_temp[i])
        # print(tbl)
        res = 0
        target = len(tbl) - 1
        worker.sort()
        for i in range(len(worker) -1, -1, -1):
            while tbl[target][0] > worker[i]:
                target -= 1
                if target < 0:
                    break
            if target >= 0:
                res += tbl[target][1]
                # print("worker[{0:d}]... {1:d}, difficulty ... {2:d}, profilt ... {3:d}".format(i, worker[i], tbl[target][0], tbl[target][1]))
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

    difficulty = [int(n) for n in flds[0].split(",")]
    profit     = [int(n) for n in flds[1].split(",")]
    worker     = [int(n) for n in flds[2].split(",")]
    print("difficulty = {0}".format(difficulty))
    print("profit     = {0}".format(profit))
    print("worker     = {0}".format(worker))

    sl = Solution()

    time0 = time.time()

    result = sl.maxProfitAssignment(difficulty, profit, worker)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
