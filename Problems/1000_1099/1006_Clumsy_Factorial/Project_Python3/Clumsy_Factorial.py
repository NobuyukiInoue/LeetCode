# coding: utf-8

import os
import sys
import time
import collections
from functools import reduce

class Solution:
#   def clumsy(self, N: int) -> int:
    def clumsy(self, N):
        # 20ma
        return [0, 1, 2, 6, 7][N] if N < 5 else N + [1, 2, 2, - 1][N % 4]

    def clumsy2(self, N):
        # 40ms
        def caltail(n):
            if n == 1: return -1
            if n == 2: return -2
            if n == 3: return -6
            if n == 4: return -5
            return caltail(n - 4) - n * (n - 1) // (n - 2) + (n - 3)
        
        if N == 1: return 1
        if N == 2: return 2
        if N == 3: return 6
        if N == 4: return 7
        return N * (N - 1) // (N - 2) + N - 3 + caltail(N - 4)

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

    N = int(flds)
    print("N = {0:d}".format(N))

    sl = Solution()
    time0 = time.time()

    result = sl.clumsy(N)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
