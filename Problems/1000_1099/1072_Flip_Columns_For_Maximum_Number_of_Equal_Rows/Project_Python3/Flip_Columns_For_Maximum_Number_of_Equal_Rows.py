# coding: utf-8

import os
import sys
import time
import collections

class Solution:
#   def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
    def maxEqualRowsAfterFlips(self, matrix: [[int]]) -> int:
        # 1496ms
        patterns = {}
        for row in matrix:
            patterns[tuple(row)] = patterns.get(tuple(row), 0) + 1
            flip = [1 - c for c in row]
            patterns[tuple(flip)] = patterns.get(tuple(flip), 0) + 1
        return max(patterns.values())

    def maxEqualRowsAfterFlips2(self, matrix: [[int]]) -> int:
        # 1572ms
        return max(collections.Counter(tuple(x ^ r[0] for x in r) for r in matrix).values())

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
    matrix = [[]]*len(flds)
    for i, _ in enumerate(matrix):
        matrix[i] = [int(n) for n in flds[i].split(",")]
    print("matrix = {0}".format(matrix))

    sl = Solution()

    time0 = time.time()

    result = sl.maxEqualRowsAfterFlips(matrix)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
