# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # 652ms
        height = len(rowSum)
        width = len(colSum)
        matrix = [[0]*width for _ in range(height)]
        i = j = 0
        while i < height and j < width:
            matrix[i][j] = min(rowSum[i], colSum[j])
            if rowSum[i] == colSum[j]:
                i += 1
                j += 1
            elif rowSum[i] > colSum[j]:
                rowSum[i] -= colSum[j]
                j += 1
            else:
                colSum[j] -= rowSum[i]
                i += 1
        return matrix

    def restoreMatrix2(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # 1168ms
        height = len(rowSum)
        width = len(colSum)
        matrix = [[0]*width for _ in range(height)]
        for y in range(height):
            for x in range(width):
                matrix[y][x] = min(rowSum[y], colSum[x])
                rowSum[y] -= matrix[y][x]
                colSum[x] -= matrix[y][x]
        return matrix

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
    rowSum = [int(n) for n in flds[0].split(",")]
    colSum = [int(n) for n in flds[1].split(",")]
    print("rowSum = {0}".format(rowSum))
    print("colSum = {0}".format(colSum))

    sl = Solution()

    time0 = time.time()

    result = sl.restoreMatrix(rowSum, colSum)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
