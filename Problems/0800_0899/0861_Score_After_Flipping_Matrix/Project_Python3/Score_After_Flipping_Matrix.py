# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        # 40ms
        r, c = len(A), len(A[0])
        answer = r * (1 << (c - 1))
        for j in range(1, c):
            count = 0
            for i in range(r):
                if A[i][0] == 1:
                    count += A[i][j]
                else:
                    count += A[i][j] ^ 1
            answer += max(r - count, count) * (1 << (c - 1 - j))
        return answer

def printGrid(title, grid):
    print("{0} = [".format(title))
    for i in range(len(grid)):
        if i == 0:
            print(" [", end = "")
        else:
            print(",[", end = "")
        for j in range(len(grid[i])):
            if j == 0:
                print("{0:d}".format(grid[i][j]), end = "")
            else:
                print(",{0:d}".format(grid[i][j]), end = "")
        print("]")
    print("]")

def printResult(title, result):
    print("{0} = [".format(title))
    for i in range(len(result)):
        print(result[i])
    print("]")

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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip()

    A = [[int(col) for col in data.split(",")] for data in flds.split("],[")]
    printGrid("A", A)
  
    sl = Solution()
    time0 = time.time()

    result = sl.matrixScore(A)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
