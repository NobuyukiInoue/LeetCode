# coding: utf-8

import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # 48ms
        oldRow = [poured]
        for i in range(query_row):
            newRow = [0]*min(i + 2, query_glass + 1)
            for j in range(len(oldRow) - 1):
                if oldRow[j] > 1:
                    newRow[j] += (oldRow[j] - 1)/2.0
                    newRow[j + 1] += (oldRow[j] - 1)/2.0
            if oldRow[-1] > 1:
                newRow[-1] += (oldRow[-1] - 1)/2.0
                if len(oldRow) < len(newRow):
                    newRow[-2] += (oldRow[-1] - 1)/2.0
            oldRow = newRow
        return min(oldRow[-1], 1)

    def champagneTower2(self, poured: int, query_row: int, query_glass: int) -> float:
        # 144ms
        res = [poured] + [0]*query_row
        for row in range(1, query_row + 1):
            for i in range(row, -1, -1):
                res[i] = max(res[i] - 1, 0) / 2.0 + max(res[i - 1] - 1, 0) / 2.0
        return min(res[query_glass], 1)

    def champagneTower_bad(self, poured: int, query_row: int, query_glass: int) -> float:
        #
        least_poured = poured
        n = 0
        while n < query_row:
            least_poured -= (n + 1)
            if least_poured < 0:
                return 0.0
            n += 1
        target_rows_poured = least_poured/(n + 1)
        if target_rows_poured >= 1.0:
            return 1.0
        return target_rows_poured

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
    flds = temp.replace("[","").replace("]","").replace(", ",",").rstrip().split(",")

    poured, query_row, query_glass = int(flds[0]), int(flds[1]), int(flds[2])
    print("poured = {0:d}, query_row = {1:d}, query_glass = {2:d}\n".format(poured, query_row, query_glass))

    sl = Solution()

    time0 = time.time()

    result = sl.champagneTower(poured, query_row, query_glass)

    time1 = time.time()

    print("result = {0:f}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
